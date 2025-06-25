# AI Service Advisor Bot

## Overview

This project is an intelligent service advisor system designed for automotive dealerships and repair shops. It automates key stages of the service write-up, diagnostic, and customer communication process using GPT agents, real-world dealership workflows, and predictive insights.

---

## Project Goals

* Reduce advisor workload
* Improve customer communication and transparency
* Increase shop efficiency and upsell conversion
* Leverage real-time data to personalize service

---

## Core Features

### 1. Customer Intake

* VIN decoding
* Appointment verification
* Primary concern categorization (maintenance, repair, recall, multi-issue)

### 2. Maintenance Advisor

* Pulls maintenance schedule by mileage
* Suggests services based on prior RO history
* Predicts likely needs based on model behavior

### 3. Recall & Bulletin Integration

* Checks for open recalls
* Pulls most current SIBs or TSBs for reported issues
* Automatically attaches relevant documents to RO

### 4. Parts Coordination

* Verifies stock levels
* Estimates pricing and delivery ETA
* Pre-pulls parts for approved work

### 5. Tech Dispatch

* ROs routed to appropriate tech based on issue
* Tech receives notes + linked SIBs/recalls

### 6. Live Customer Updates

* Notifies customer on major steps (check-in, diag complete, approval needed, ready)
* Option to automate 2nd-phase approvals based on thresholds

### 7. Transportation Logic

* Waiter/loaner logic triggered by RO time estimation
* Complimentary loaner if >3hr approved services

### 8. Final Delivery & Retention

* Completion message
* Surveys & feedback capture
* RO data returned to customer profile for next visit

---

## Data Stack

* **SQL:** Used to analyze past RO history, tier customers, and generate upsell flags
* **Flask API:** Powers webhooks and triggers for communication
* **GPT (ChatGPT/GPT-4):** Handles natural language intake, issue decoding, and customer interaction
* **Vector Memory (planned):** To retain service history context over time

---

## AI Agent Stack

This project uses modular GPT agents for specific roles:

* Intake Agent
* Maintenance Advisor
* Recall & SIB Agent
* Parts Agent
* Tech Routing Agent
* Customer Update Agent
* Transport/Loaner Agent
* Post-Service Agent

Each agent runs in isolation but communicates through shared memory and structured output.

---

## Sample SQL Use Cases

```sql
-- Flag high-value customers
SELECT customer_id, COUNT(*) as visits, AVG(total) as avg_spend
FROM repair_orders
GROUP BY customer_id
HAVING visits > 3 AND avg_spend > 800;

-- Declined coolant flushes
SELECT * FROM declined_services
WHERE service_name ILIKE '%coolant flush%';
```

---

## Future Roadmap

* Add vector DB memory to track customer personalities/preferences
* Build drag-and-drop UI for advisors to review GPT suggestions
* Integrate with live DMS platforms (CDK, Reynolds & Reynolds)
* Add multilingual support

---

## Why This Matters

This bot isn’t just automation. It’s a rethink of how we deliver trust, speed, and insight to customers walking into a dealership. It combines frontline logic with backend intelligence to make every visit feel tailored, proactive, and frictionless.

---

## Author

**SFAZ615**
Builder | Operator | GPT Dev

