resource "aws_vpc" "this" {

  cidr_block = "10.0.0.0/16"

  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "${var.project_name}-${var.environment}-vpc"
  }
}

resource "aws_subnet" "private_a" {

  vpc_id = aws_vpc.this.id

  cidr_block = "10.0.1.0/24"

  availability_zone = "ap-south-1a"

  tags = {
    Name = "${var.project_name}-${var.environment}-private-a"
  }
}

resource "aws_subnet" "private_b" {

  vpc_id = aws_vpc.this.id

  cidr_block = "10.0.2.0/24"

  availability_zone = "ap-south-1b"

  tags = {
    Name = "${var.project_name}-${var.environment}-private-b"
  }
}

resource "aws_security_group" "aurora" {

  name = "${var.project_name}-${var.environment}-aurora-sg"

  vpc_id = aws_vpc.this.id

  ingress {

    from_port = 5432
    to_port   = 5432

    protocol = "tcp"

    cidr_blocks = [
      "10.0.0.0/16"
    ]
  }

  egress {

    from_port = 0
    to_port   = 0

    protocol = "-1"

    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }
}

resource "aws_security_group" "dms" {

  name = "${var.project_name}-${var.environment}-dms-sg"

  vpc_id = aws_vpc.this.id

  egress {

    from_port = 0
    to_port   = 0

    protocol = "-1"

    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }
}

resource "aws_db_subnet_group" "aurora" {

  name = "${var.project_name}-${var.environment}-db-subnet-group"

  subnet_ids = [
    aws_subnet.private_a.id,
    aws_subnet.private_b.id
  ]

  tags = {
    Name = "${var.project_name}-${var.environment}-db-subnet-group"
  }
}


