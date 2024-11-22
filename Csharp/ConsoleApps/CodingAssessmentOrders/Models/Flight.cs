namespace CodingAssessmentOrders.Models
{
    public class Flight
    {
        public int FlightId { get; set; }
        public string Departure { get; set; } = string.Empty;
        public string Arrival { get; set; } = string.Empty;
        public int Day { get; set; }
        public int Capacity { get; set; }
        public List<Order> LoadedOrders { get; set; } = new List<Order>();
    }
}