CREATE SCHEMA IF NOT EXISTS payment;

CREATE TABLE IF NOT EXISTS payment.invoice (
    invoice_id VARCHAR(32) PRIMARY KEY,
    subscription_id VARCHAR(32) NOT NULL,
    account_id VARCHAR(32) NOT NULL,
    invoice_date DATE NOT NULL,
    amount_due NUMERIC(10,2) NOT NULL,
    invoice_status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_invoice_subscription
        FOREIGN KEY (subscription_id)
        REFERENCES subscription.subscription(subscription_id),

    CONSTRAINT fk_invoice_account
        FOREIGN KEY (account_id)
        REFERENCES account.account(account_id)
);

CREATE TABLE IF NOT EXISTS payment.payment (
    payment_id VARCHAR(32) PRIMARY KEY,
    invoice_id VARCHAR(32) NOT NULL,
    payment_date DATE NOT NULL,
    payment_amount NUMERIC(10,2) NOT NULL,
    payment_method VARCHAR(30) NOT NULL,
    payment_status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_payment_invoice
        FOREIGN KEY (invoice_id)
        REFERENCES payment.invoice(invoice_id)
);