output "vpc_id" {

  value = aws_vpc.this.id
}

output "private_subnet_ids" {

  value = [
    aws_subnet.private_a.id,
    aws_subnet.private_b.id
  ]
}

output "aurora_security_group_id" {

  value = aws_security_group.aurora.id
}

output "dms_security_group_id" {

  value = aws_security_group.dms.id
}

output "db_subnet_group_name" {

  value = aws_db_subnet_group.aurora.name
}
