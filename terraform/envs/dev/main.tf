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


module "dms" {

  source = "../../modules/dms"

  environment = var.environment

  dms_security_group_id = module.network.dms_security_group_id

  private_subnet_ids = module.network.private_subnet_ids

  aurora_endpoint = module.aurora.cluster_endpoint

  database_name = "netflix"

  db_username = var.db_username
  db_password = var.db_password

  bucket_name = module.s3.bucket_name

  dms_s3_role_arn = module.iam.dms_role_arn
}