module "network" {

  source = "../../modules/network"

  project_name = var.project_name
  environment  = var.environment
}

module "s3" {

  source = "../../modules/s3"

  project_name = var.project_name
  environment  = var.environment
}

module "iam" {

  source = "../../modules/iam"

  project_name = var.project_name
  environment  = var.environment
}

module "aurora" {

  source = "../../modules/aurora"

  project_name = var.project_name
  environment  = var.environment

  db_subnet_group_name = module.network.db_subnet_group_name

  security_group_id = module.network.aurora_security_group_id
}