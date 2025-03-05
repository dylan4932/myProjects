using System;
using System.Collections.Generic;
using CodingAssessmentOrders.Models;

namespace CodingAssessmentOrders.Controllers
{
    public class OrderController
    {
        private readonly List<Flight> _flights;
        private readonly Queue<Order> _orderQueue;

        static readonly List<string> _orderPriority = new List<string>{
            "same-day",
            "next-day",
            "regular"
        };

        public OrderController(List<Flight> flights)
        {
            _flights = flights;
            _orderQueue = new Queue<Order>();
        }

        public void ProcessOrders(List<Order> orders)
        {
            List<Order> sortedOrders = orders.OrderBy(i => _orderPriority.IndexOf(i.Service)).ToList();
            foreach (var order in sortedOrders)
            {
                _orderQueue.Enqueue(order);
            }
        }

        public void ScheduleOrders()
        {
            while (_orderQueue.Count > 0)
            {
                var order = _orderQueue.Dequeue();
                bool isScheduled = false;

                foreach (var flight in _flights)
                {
                    if (flight.Arrival == order.Destination && flight.LoadedOrders.Count < flight.Capacity)
                    {
                        flight.LoadedOrders.Add(order);
                        order.IsScheduled = true;
                        isScheduled = true;
                        break;
                    }
                }

                if (!isScheduled)
                {
                    Console.WriteLine($"Order: {order.OrderId} is not scheduled.");
                }
            }
        }

        public void DisplayOrders(List<int> flightIdToCheck)
        {
            Flight? flightToCheckObj = _flights.Find(flight => flightIdToCheck.Contains(flight.FlightId)) ?? null;
            if (flightToCheckObj!= null) {
                foreach (var order in flightToCheckObj.LoadedOrders){
                    Console.WriteLine($"Order: {order.OrderId} service-level: {order.Service}, FlightId: {flightToCheckObj.FlightId}, Departure: {flightToCheckObj.Departure}, Arrival: {flightToCheckObj.Arrival}, Day: {flightToCheckObj.Day}");
                }
            } else {
                Console.WriteLine("No flight found.");
            }
            
        }

        public void DisplayAllOrders()
        {
            foreach(Flight flight in _flights) {
                foreach(var order in flight.LoadedOrders) {
                    Console.WriteLine($"Order: {order.OrderId} service-level: {order.Service}, FlightId: {flight.FlightId}, Departure: {flight.Departure}, Arrival: {flight.Arrival}, Day: {flight.Day}");
                }
            }
        }
    }
}