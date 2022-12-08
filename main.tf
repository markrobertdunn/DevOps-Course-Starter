terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }
  backend "azurerm" {
    resource_group_name  = "OpenCohort21_MarkDunn_ProjectExercise"
    storage_account_name = "open21markdunnstorageacc"
    container_name       = "todoapp"
    key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name = "OpenCohort21_MarkDunn_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name                = "${var.prefix}-terraformed-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"
}
resource "azurerm_linux_web_app" "main" {
  name                = "${var.prefix}-devopstodoapp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id
  site_config {
    application_stack {
      docker_image     = "markrobertdunn/todo-app"
      docker_image_tag = "latest"
    }
  }
  app_settings = {
    "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
    "CONNECTIONSTRING"           = azurerm_cosmosdb_account.main.connection_strings[0]
    "SECRET_KEY"                 = var.secret_key
  }
}

resource "azurerm_cosmosdb_account" "main" {
  name                = "${var.prefix}-tfdevopstodoapp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"

  enable_automatic_failover = true

  capabilities {
    name = "EnableAggregationPipeline"
  }

  capabilities {
    name = "mongoEnableDocLevelTTL"
  }

  capabilities {
    name = "MongoDBv3.4"
  }

  capabilities {
    name = "EnableMongo"
  }

  capabilities {
    name = "EnableServerless"
  }

  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }
  geo_location {
    location          = "westus"
    failover_priority = 0
  }
}


resource "azurerm_cosmosdb_mongo_database" "main" {
  name                = "${var.prefix}-test-database"
  resource_group_name = "OpenCohort21_MarkDunn_ProjectExercise"
  account_name        = azurerm_cosmosdb_account.main.name
  lifecycle {
    prevent_destroy = false
  }
}

