terraform {
    required_providers {
        azurerm = {
            source = "hashicorp/azurerm"
            version = ">= 3.8"
        }
    }
}

provider "azurerm" {
 features {}
}

data "azurerm_resource_group" "main" {
  name = "OpenCohort21_MarkDunn_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name = "terraformed-asp" 
  location = data.azurerm_resource_group.main.location 
  resource_group_name = data.azurerm_resource_group.main.name 
  os_type = "Linux"
  sku_name = "B1"
}
resource "azurerm_linux_web_app" "main" {
  name = "markdunntodotest" 
  location = data.azurerm_resource_group.main.location 
  resource_group_name = data.azurerm_resource_group.main.name 
  service_plan_id = azurerm_service_plan.main.id 
  site_config { 
  application_stack { 
    docker_image = "appsvcsample/python-helloworld" 
    docker_image_tag = "latest" 
  } 
  } 
  app_settings = { 
  "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io" 
  }
}

resource "azurerm_resource_group" "example" {
  name     = "example-resource-group"
  location = "West Europe"
}

resource "random_integer" "ri" {
  min = 10000
  max = 99999
}

resource "azurerm_cosmosdb_account" "db" {
  name                = "tfex-cosmos-db-${random_integer.ri.result}"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
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
    location          = "eastus"
    failover_priority = 1
  }

  geo_location {
    location          = "westus"
    failover_priority = 0
  }
}

data "azurerm_cosmosdb_account" "todoapp" {
  name                = "Mark.Dunn@softwireacademy.onmicrosoft.com"
  resource_group_name = "OpenCohort21_MarkDunn_ProjectExercise"
}

resource "azurerm_cosmosdb_mongo_database" "todoapp" {
  name                = "test-database"
  resource_group_name = data.azurerm_cosmosdb_account.todoapp.OpenCohort21_MarkDunn_ProjectExercise
  account_name        = data.azurerm_cosmosdb_account.todoappp.test-database
  throughput          = 400
}