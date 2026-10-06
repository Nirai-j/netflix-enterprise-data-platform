CREATE SCHEMA IF NOT EXISTS subscription;

CREATE TABLE IF NOT EXISTS subscription.plan (
    plan_id VARCHAR(32) PRIMARY KEY,
    plan_name VARCHAR(100) NOT NULL,
    monthly_price NUMERIC(10,2) NOT NULL,
    currency VARCHAR(10) NOT NULL,
    max_screens INTEGER NOT NULL,
    video_quality VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS subscription.subscription (
    subscription_id VARCHAR(32) PRIMARY KEY,
    account_id VARCHAR(32) NOT NULL,
    plan_id VARCHAR(32) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_subscription_account
        FOREIGN KEY (account_id)
        REFERENCES account.account(account_id),

    CONSTRAINT fk_subscription_plan
        FOREIGN KEY (plan_id)
        REFERENCES subscription.plan(plan_id)
);