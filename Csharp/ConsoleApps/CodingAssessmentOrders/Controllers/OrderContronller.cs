using System;
using System.Collections.Generic;
using CodingAssessmentOrders.Models;

namespace CodingAssessmentOrders.Controllers
{
    public class OrderController
    {
        private readonly List<Flight> _flights;
        private readonly Queue<Order> _orderQueue;

        public OrderController(List<Flight> flights)
        {
            _flights = flights;
            _orderQueue = new Queue<Order>();
        }

        public void ProcessOrders(List<Order> orders)
        {
            foreach (var order in orders)
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

        public void DisplayOrders()
        {
            foreach (var flight in _flights)
            {
                foreach (var order in flight.LoadedOrders)
                {
                    Console.WriteLine($"Order: {order.OrderId}, FlightId: {flight.FlightId}, Departure: {flight.Departure}, Arrival: {flight.Arrival}, Day: {flight.Day}");
                }
            }
        }
    }
}