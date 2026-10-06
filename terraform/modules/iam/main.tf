resource "aws_iam_role" "dms_s3_role" {

  name = "${var.project_name}-${var.environment}-dms-s3-role"

  assume_role_policy = jsonencode({

    Version = "2012-10-17"

    Statement = [

      {
        Effect = "Allow"

        Principal = {
          Service = "dms.amazonaws.com"
        }

        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy" "dms_s3_policy" {

  name = "dms-s3-policy"

  role = aws_iam_role.dms_s3_role.id

  policy = jsonencode({

    Version = "2012-10-17"

    Statement = [

      {
        Effect = "Allow"

        Action = [
          "s3:*"
        ]

        Resource = "*"
      }
    ]
  })
}