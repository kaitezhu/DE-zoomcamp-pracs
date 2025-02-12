variable "credentials" {
  description = "My Credentials"
  default     = "/home/ktzhu/.gc/g_cred.json"
}

variable "project" {
  description = "Project"
  default     = "dtc-de-course-449111"
}

variable "region" {
  description = "Project Region"
  default     = "australia-southeast2"
}

variable "location" {
  description = "Project Location"
  default     = "australia-southeast2"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "dtc-de-course-449111-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}