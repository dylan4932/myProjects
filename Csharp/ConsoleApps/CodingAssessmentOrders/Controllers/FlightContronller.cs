using System;
using System.Collections.Generic;
using CodingAssessmentOrders.Models;

namespace CodingAssessmentOrders.Controllers
{
    public class FlightController
    {
        public List<Flight> Flights { get; private set; }

        public FlightController()
        {
            Flights = new List<Flight>();
        }

        public void Initialize()
        {
            Flights.Add(new Flight { FlightId = 1, Departure = "YUL", Arrival = "YYZ", Day = 1, Capacity = 20 });
            Flights.Add(new Flight { FlightId = 2, Departure = "YUL", Arrival = "YYC", Day = 1, Capacity = 20 });
            Flights.Add(new Flight { FlightId = 3, Departure = "YUL", Arrival = "YVR", Day = 1, Capacity = 20 });
            Flights.Add(new Flight { FlightId = 4, Departure = "YUL", Arrival = "YYZ", Day = 2, Capacity = 20 });
            Flights.Add(new Flight { FlightId = 5, Departure = "YUL", Arrival = "YYC", Day = 2, Capacity = 20 });
            Flights.Add(new Flight { FlightId = 6, Departure = "YUL", Arrival = "YVR", Day = 2, Capacity = 20 });
        }

        public void DisplayFlights()
        {
            foreach (var flight in Flights)
            {
                Console.WriteLine($"Flight: {flight.FlightId}, Departure: {flight.Departure}, Arrival: {flight.Arrival}, Day: {flight.Day}");
            }
        }
    }
}