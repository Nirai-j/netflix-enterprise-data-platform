CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.title (
    content_id VARCHAR(32) PRIMARY KEY,
    title_name VARCHAR(255) NOT NULL,
    content_type VARCHAR(20) NOT NULL,
    genre VARCHAR(50),
    release_year INTEGER,
    rating VARCHAR(20),
    duration_minutes INTEGER,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS content.season (
    season_id VARCHAR(32) PRIMARY KEY,
    content_id VARCHAR(32) NOT NULL,
    season_number INTEGER NOT NULL,

    CONSTRAINT fk_season_title
        FOREIGN KEY (content_id)
        REFERENCES content.title(content_id)
);

CREATE TABLE IF NOT EXISTS content.episode (
    episode_id VARCHAR(32) PRIMARY KEY,
    season_id VARCHAR(32) NOT NULL,
    episode_number INTEGER NOT NULL,
    duration_minutes INTEGER NOT NULL,

    CONSTRAINT fk_episode_season
        FOREIGN KEY (season_id)
        REFERENCES content.season(season_id)
);