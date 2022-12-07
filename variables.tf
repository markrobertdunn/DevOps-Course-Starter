variable "prefix" {
  description = "The prefix used for all resources in this environment"
}

variable "secret_key" {
  description = "Secret Key"
  sensitive   = true
}
