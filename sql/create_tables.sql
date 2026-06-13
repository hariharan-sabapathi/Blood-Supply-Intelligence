CREATE DATABASE blood_supply;

CREATE TABLE blood_supply_metrics
(
    blood_type VARCHAR(10),
    avg_inventory NUMERIC,
    total_received NUMERIC,
    total_used NUMERIC,
    emergency_requests NUMERIC,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);