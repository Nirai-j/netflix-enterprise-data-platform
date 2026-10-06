resource "aws_s3_bucket" "landing" {

  bucket = "${var.project_name}-${var.environment}-landing"
}

resource "aws_s3_bucket_public_access_block" "landing" {

  bucket = aws_s3_bucket.landing.id

  block_public_acls       = true
  block_public_policy     = true

  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "landing" {

  bucket = aws_s3_bucket.landing.id

  versioning_configuration {

    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "landing" {

  bucket = aws_s3_bucket.landing.id

  rule {

    apply_server_side_encryption_by_default {

      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_object" "landing_account" {

  bucket = aws_s3_bucket.landing.id

  key    = "landing/account/"
}

resource "aws_s3_object" "landing_subscription" {

  bucket = aws_s3_bucket.landing.id

  key    = "landing/subscription/"
}

resource "aws_s3_object" "landing_payment" {

  bucket = aws_s3_bucket.landing.id

  key    = "landing/payment/"
}

resource "aws_s3_object" "landing_content" {

  bucket = aws_s3_bucket.landing.id

  key    = "landing/content/"
}

resource "aws_s3_object" "cdc" {

  bucket = aws_s3_bucket.landing.id

  key    = "cdc/"
}

resource "aws_s3_object" "checkpoints" {

  bucket = aws_s3_bucket.landing.id

  key    = "checkpoints/"
}