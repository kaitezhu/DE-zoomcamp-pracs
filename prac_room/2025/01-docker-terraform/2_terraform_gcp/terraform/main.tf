terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.18.1"
    }
  }
}

provider "google" {
  project = "dtc-de-course-449111"
  region  = "australia-southeast2"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "dtc-de-course-449111"
  location      = "australia-southeast2"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}