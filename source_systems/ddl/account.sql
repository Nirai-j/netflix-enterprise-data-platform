CREATE SCHEMA IF NOT EXISTS account;

CREATE TABLE IF NOT EXISTS account.account (
    account_id VARCHAR(32) PRIMARY KEY,
    country VARCHAR(10) NOT NULL,
    signup_date DATE NOT NULL,
    acquisition_channel VARCHAR(50),
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS account.profile (
    profile_id VARCHAR(32) PRIMARY KEY,
    account_id VARCHAR(32) NOT NULL,
    profile_type VARCHAR(20) NOT NULL,
    language VARCHAR(20),
    created_date DATE NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_profile_account
        FOREIGN KEY (account_id)
        REFERENCES account.account(account_id)
);