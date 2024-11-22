using System;
using System.Collections.Generic;
using CodingAssessmentOrders.Models;

namespace CodingAssessmentOrders.Controllers
{
    public class OrderQueue
    {
        private readonly Queue<Order> _orderQueue;

        public OrderQueue()
        {
            _orderQueue = new Queue<Order>();
        }

        public void EnqueueOrder(Order order)
        {
            _orderQueue.Enqueue(order);
        }

        public Order DequeueOrder()
        {
            if (_orderQueue.Count == 0)
            {
                throw new InvalidOperationException("The OrderQueue is empty.");
            }

            var order = _orderQueue.Dequeue();
            return order;
        }

        public bool IsEmpty()
        {
            return _orderQueue.Count == 0;
        }

        public int Count()
        {
            return _orderQueue.Count;
        }
    }
}