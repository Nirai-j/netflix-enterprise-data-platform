resource "aws_rds_cluster" "aurora" {

  cluster_identifier = "${var.project_name}-${var.environment}-aurora"

  engine         = "aurora-postgresql"
  engine_version = "14.24"

  master_username = "netflix_admin"
  master_password = "Netflix123!"

  backup_retention_period = 1
  
  db_subnet_group_name = var.db_subnet_group_name

  vpc_security_group_ids = [
    var.security_group_id
  ]

  skip_final_snapshot = true

  storage_encrypted = true
}


resource "aws_rds_cluster_instance" "aurora" {

  identifier = "${var.project_name}-${var.environment}-aurora-instance"

  cluster_identifier = aws_rds_cluster.aurora.id

  instance_class = "db.t4g.medium"

  engine = aws_rds_cluster.aurora.engine

  publicly_accessible = true
}