provider "aws" {

  region = var.aws_region

  default_tags {

    tags = {
      Project     = "Netflix"
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}