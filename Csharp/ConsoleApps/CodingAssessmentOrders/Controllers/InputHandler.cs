using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Text.Json.Serialization;
using CodingAssessmentOrders.Models;

namespace CodingAssessmentOrders.Controllers
{
    public class InputHandler
    {
        public List<Order> GenerateOrders()
        {
            List<Order> orders = new List<Order>();
            Console.WriteLine("Choose an option:");
            Console.WriteLine("1. Input orders from file");
            Console.WriteLine("2. Input orders manually");
            Console.WriteLine("3. Exit");
            Console.Write("Enter your choice (1, 2, or 3): ");
            string? choice = Console.ReadLine()?.Trim();

            switch (choice)
            {
                case "1":
                    Console.Write("Enter the file path: ");
                    string? filePath = Console.ReadLine()?.Trim();

                    if (!string.IsNullOrWhiteSpace(filePath))
                    {
                        orders = this.ReadOrdersFromFile(filePath);
                        if (orders.Count > 0)
                        {
                            Console.WriteLine("Orders loaded successfully from file.");
                        }
                        else
                        {
                            Console.WriteLine("No orders loaded. Please check the file.");
                        }
                    }
                    else
                    {
                        Console.WriteLine("Invalid file path. Please try again.");
                    }
                    break;

                case "2":
                    orders = this.ReadFromUserInput();
                    if (orders.Count > 0)
                    {
                        Console.WriteLine("Orders entered successfully.");
                    }
                    else
                    {
                        Console.WriteLine("No orders entered.");
                    }
                    break;

                case "3":
                    Console.WriteLine("Exiting the program. Goodbye!");
                    return new List<Order>();

                default:
                    Console.WriteLine("Invalid choice. Please try again.");
                    break;
            }

            return orders;
        }

        public List<Order> ReadFromUserInput()
        {
            var orders = new List<Order>();
            Console.WriteLine("Enter order details. Type 'done' to finish.");

            while (true)
            {
                Console.Write("Enter Order ID (or type 'done' to finish): ");
                string? orderId = Console.ReadLine()?.Trim();

                if (string.Equals(orderId, "done", StringComparison.OrdinalIgnoreCase))
                {
                    break;
                }
                if (string.IsNullOrWhiteSpace(orderId))
                {
                    Console.WriteLine("Order ID cannot be empty. Please try again.");
                    continue;
                }

                Console.Write("Enter Destination: ");
                string? destination = Console.ReadLine()?.Trim();

                if (string.IsNullOrWhiteSpace(destination))
                {
                    Console.WriteLine("Destination cannot be empty. Please try again.");
                    continue;
                }

                var newOrder = new Order
                {
                    OrderId = orderId,
                    Destination = destination,
                    IsScheduled = false
                };
                orders.Add(newOrder);

                Console.WriteLine($"Order {orderId} added successfully!");
            }

            Console.WriteLine("Order input completed.");
            return orders;
        }

        public List<Order> ReadOrdersFromFile(string filePath)
        {
            if (!File.Exists(filePath))
            {
                Console.WriteLine($"File not found: {filePath}");
                return new List<Order>();
            }

            try
            {
                string jsonContent = File.ReadAllText(filePath);
                var options = new JsonSerializerOptions
                {
                    PropertyNameCaseInsensitive = true
                };

                Dictionary<string, Order>? OrdersContent = JsonSerializer.Deserialize<Dictionary<string, Order>>(jsonContent, options);

                if (OrdersContent == null)
                {
                    Console.WriteLine("No data found in the file.");
                    return new List<Order>();
                }

                var orders = new List<Order>();
                foreach (var content in OrdersContent)
                {
                    var newOrder = new Order
                    {
                        OrderId = content.Key,
                        Destination = content.Value?.Destination ?? "Unknown",
                        IsScheduled = false, // Default value
                        Service = content.Value?.Service ?? "regular"
                    };
                    orders.Add(newOrder);
                }
                return orders;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred while reading the data: {ex.Message}");
                return new List<Order>();
            }
        }
    }
}
