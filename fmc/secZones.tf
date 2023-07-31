#Jeff Comer


#data "fmc_access_policies" "access_policy" {
#    name = "FTD"
#}

resource "fmc_security_zone" "INSIDE" {
    name = "INSIDE"
    interface_mode = "INLINE"
}

resource "fmc_security_zone" "OUTSIDE" {
    name = "OUTSIDE"
    interface_mode = "INLINE"
}

resource "fmc_security_zone" "DMZ" {
    name = "DMZ"
    interface_mode = "INLINE"
}