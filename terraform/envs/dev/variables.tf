variable "aws_region" {
  type = string
}

variable "environment" {
  type = string
}

variable "project_name" {
  type = string
}

variable "db_username" {}
variable "db_password" {
  sensitive = true
}