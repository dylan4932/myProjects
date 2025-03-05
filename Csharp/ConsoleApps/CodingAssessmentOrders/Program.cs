using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Text.Json.Serialization;
using CodingAssessmentOrders.Models;
using CodingAssessmentOrders.Controllers;

class Program
{   
    static void Main(string[] args)
    {
        var inputHandler = new InputHandler();
        // string filePath = "./Resources/orders-data.json";
        List<Order> orders = inputHandler.GenerateOrders();

        if (orders == null || orders.Count == 0)
        {
            Console.WriteLine("No orders found.");
            return;
        }

        var scheduleService = new FlightController();
        scheduleService.Initialize();

        var orderService = new OrderController(scheduleService.Flights);
        orderService.ProcessOrders(orders);
        orderService.ScheduleOrders();

        Console.WriteLine("\nOrder Itineraries:");

        // int flightIdToCheck = 5;
        orderService.DisplayAllOrders();
    }

}
