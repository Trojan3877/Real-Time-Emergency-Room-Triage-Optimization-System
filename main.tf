provider "aws" {
  region = "us-west-2"
}

resource "aws_vpc" "meditriage_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "meditriage_subnet" {
  vpc_id                  = aws_vpc.meditriage_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-west-2a"
  map_public_ip_on_launch = true
}

resource "aws_eks_cluster" "meditriage_cluster" {
  name     = "meditriage-eks-cluster"
  role_arn = "arn:aws:iam::YOUR_ACCOUNT_ID:role/EKSClusterRole"

  vpc_config {
    subnet_ids = [aws_subnet.meditriage_subnet.id]
  }

  depends_on = [aws_subnet.meditriage_subnet]
}
