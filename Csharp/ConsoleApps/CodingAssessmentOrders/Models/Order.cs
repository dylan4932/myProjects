namespace CodingAssessmentOrders.Models
{
    public class Order
    {
        public string OrderId { get; set; } = string.Empty;
        public string Destination { get; set; } = string.Empty;
        public bool IsScheduled { get; set; } = false;
        public string Service { get; set; } = "regular"; 
    }
}