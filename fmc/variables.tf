variable "fmc_username" {
    type = string
    sensitive = true
}

variable "fmc_password" {
    type = string
    sensitive = true
}

variable "fmc_host" {
    type = string
}

variable "fmc_insecure_skip_verify" {
    type = bool
    default = false
}

variable "fmc_regkey" {
    type = string
}

variable "fmc_ftd1" {
    type = string
}

variable "fmc_ftd1_name" {
    type = string
}