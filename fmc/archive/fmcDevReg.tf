#Jeff Comer


#data "fmc_access_policies" "access_policy" {
#    name = "FTD"
#}

resource "fmc_access_policies" "access_policy" {
    name = "dcloud-accessPolicy"
    default_action = "permit"
}

resource "fmc_access_rules" "access_rule_urlMon" {
    acp = fmc_access_policies.access_policy.id
    section = "mandatory"
    name = "URL Monitor"
    action = "monitor"
    enabled = true
    enable_syslog = false
    #syslog_severity = "alert"
    send_events_to_fmc = true
    log_files = false
    log_end = true
}

resource "fmc_access_rules" "access_rule_threatInspect" {
    acp = fmc_access_policies.access_policy.id
    section = "mandatory"
    name = "Threat Inspection"
    action = "allow"
    enabled = true
    enable_syslog = false
    #syslog_severity = "alert"
    send_events_to_fmc = true
    log_files = false
    log_end = true
}

resource "fmc_devices" "dcloud_ftd" {
    name = var.fmc_ftd1_name
    hostname = var.fmc_ftd1
    regkey = var.fmc_regkey
    type = "Device"
    access_policy {
        id = fmc_access_policies.access_policy.id
        type = fmc_access_policies.access_policy.type
    }
}

resource "fmc_ftd_deploy" "ftd" {
    device = fmc_devices.dcloud_ftd.id
    ignore_warning = true
    force_deploy = true
}