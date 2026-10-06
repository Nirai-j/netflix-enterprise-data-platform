output "cluster_endpoint" {

  value = aws_rds_cluster.aurora.endpoint
}

output "cluster_id" {

  value = aws_rds_cluster.aurora.id
}