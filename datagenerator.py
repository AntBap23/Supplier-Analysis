{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOTbMuFdDOi+boUlo3tHuqv"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "collapsed": true,
        "id": "lsjfvgf00EAF",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "798e8648-e223-4570-d202-9e534b19d5fb"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_dbfebe86-7ef5-4cd2-ba64-0c8b270ceacf\", \"supplier_data.csv\", 63718)"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_d530ee6e-d848-46eb-9d6b-d33cb82b3af9\", \"procurement_orders.csv\", 40723)"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_37f68adf-f0d8-44b9-a2e8-9420f19c1a4a\", \"product_data.csv\", 7835)"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_3fed73e7-0a9b-4657-b3bb-b4937ecc8f00\", \"logistics_data.csv\", 31200)"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_105572e4-8e0d-4d58-b0d7-c7cf0f4845bf\", \"financial_data.csv\", 34549)"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CSV files generated and ready for download!\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "from google.colab import files\n",
        "\n",
        "# Seed for reproducibility\n",
        "np.random.seed(42)\n",
        "\n",
        "# Define the number of rows\n",
        "num_rows = 1000\n",
        "\n",
        "# Supplier Data\n",
        "def generate_supplier_data():\n",
        "    suppliers = [\n",
        "        \"Acme Corp\", \"Global Supplies\", \"Elite Manufacturing\", \"Universal Traders\", \"NextGen Logistics\",\n",
        "        \"Prime Distributors\", \"Quantum Materials\", \"Summit Components\", \"Pinnacle Products\", \"Apex Solutions\",\n",
        "        \"Velocity Ventures\", \"Fusion Industries\", \"Eagle Enterprises\", \"Silverline Co.\", \"Vanguard Supplies\",\n",
        "        \"Nova Exports\", \"Everest Goods\", \"Horizon Distributors\", \"Cascade Traders\", \"Alpha Resources\",\n",
        "        \"Beta Solutions\", \"Gamma Industries\", \"Delta Logistics\", \"Zeta Corp\", \"Omni Supplies\",\n",
        "        \"Infinity Goods\", \"Synergy Co.\", \"Genesis Materials\", \"Phoenix Products\", \"Titan Ventures\",\n",
        "        \"Atlas Components\", \"Orion Enterprises\", \"Cosmos Distributors\", \"Echo Materials\", \"Legacy Supplies\",\n",
        "        \"Momentum Goods\", \"Prime Horizons\", \"Vision Logistics\", \"Summit Exports\", \"Nexus Components\",\n",
        "        \"Pioneer Products\", \"Helix Industries\", \"Apollo Supplies\", \"Stellar Goods\", \"Zenith Distributors\"\n",
        "    ]\n",
        "    regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']\n",
        "    industries = ['Electronics', 'Automotive', 'Food', 'Textiles', 'Chemicals']\n",
        "\n",
        "    data = {\n",
        "        'SupplierID': np.arange(1, num_rows + 1),\n",
        "        'SupplierName': np.random.choice(suppliers, num_rows),\n",
        "        'Region': np.random.choice(regions, num_rows),\n",
        "        'Industry': np.random.choice(industries, num_rows),\n",
        "        'Rating': np.random.randint(1, 6, num_rows),\n",
        "        'AnnualSpendUSD': np.random.randint(5000, 500000, num_rows),\n",
        "        'OnTimeDeliveryRate': np.round(np.random.uniform(80, 100, num_rows), 2),\n",
        "        'DefectRate': np.round(np.random.uniform(0, 5, num_rows), 2),\n",
        "        'SupplierSince': np.random.randint(2000, 2023, num_rows)\n",
        "    }\n",
        "    return pd.DataFrame(data)\n",
        "\n",
        "# Procurement Orders\n",
        "def generate_procurement_orders():\n",
        "    order_ids = [f\"ORD_{i}\" for i in range(1, num_rows + 1)]\n",
        "    payment_methods = ['Credit Card', 'Bank Transfer', 'Cash']\n",
        "\n",
        "    data = {\n",
        "        'OrderID': order_ids,\n",
        "        'SupplierID': np.random.randint(1, 51, num_rows),\n",
        "        'OrderDate': pd.to_datetime(np.random.choice(pd.date_range('2022-01-01', '2023-01-01'), num_rows)),\n",
        "        'OrderValueUSD': np.random.randint(100, 50000, num_rows),\n",
        "        'PaymentMethod': np.random.choice(payment_methods, num_rows),\n",
        "        'LeadTimeDays': np.random.randint(1, 90, num_rows)\n",
        "    }\n",
        "    return pd.DataFrame(data)\n",
        "\n",
        "# Product Details\n",
        "def generate_product_data():\n",
        "    products = [f\"Product_{i}\" for i in range(1, 201)]\n",
        "    categories = ['Raw Materials', 'Components', 'Finished Goods']\n",
        "\n",
        "    data = {\n",
        "        'ProductID': np.arange(1, 201),\n",
        "        'ProductName': products,\n",
        "        'Category': np.random.choice(categories, 200),\n",
        "        'UnitPriceUSD': np.round(np.random.uniform(5, 500, 200), 2),\n",
        "        'StockQuantity': np.random.randint(0, 1000, 200)\n",
        "    }\n",
        "    return pd.DataFrame(data)\n",
        "\n",
        "# Logistics Data\n",
        "def generate_logistics_data():\n",
        "    transport_modes = ['Air', 'Sea', 'Rail', 'Road']\n",
        "    regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']\n",
        "\n",
        "    data = {\n",
        "        'LogisticsID': np.arange(1, num_rows + 1),\n",
        "        'SupplierID': np.random.randint(1, 51, num_rows),\n",
        "        'TransportMode': np.random.choice(transport_modes, num_rows),\n",
        "        'ShippingRegion': np.random.choice(regions, num_rows),\n",
        "        'ShippingCostUSD': np.round(np.random.uniform(100, 5000, num_rows), 2),\n",
        "        'DeliveryDays': np.random.randint(1, 30, num_rows)\n",
        "    }\n",
        "    return pd.DataFrame(data)\n",
        "\n",
        "# Financial Analysis\n",
        "def generate_financial_data():\n",
        "    currencies = ['USD', 'EUR', 'JPY', 'GBP']\n",
        "\n",
        "    data = {\n",
        "        'TransactionID': np.arange(1, num_rows + 1),\n",
        "        'SupplierID': np.random.randint(1, 51, num_rows),\n",
        "        'TransactionAmount': np.round(np.random.uniform(500, 10000, num_rows), 2),\n",
        "        'Currency': np.random.choice(currencies, num_rows),\n",
        "        'TransactionDate': pd.to_datetime(np.random.choice(pd.date_range('2022-01-01', '2023-01-01'), num_rows)),\n",
        "        'ExchangeRateToUSD': np.round(np.random.uniform(0.5, 1.5, num_rows), 2)\n",
        "    }\n",
        "    return pd.DataFrame(data)\n",
        "\n",
        "# Generate data\n",
        "supplier_data = generate_supplier_data()\n",
        "procurement_orders = generate_procurement_orders()\n",
        "product_data = generate_product_data()\n",
        "logistics_data = generate_logistics_data()\n",
        "financial_data = generate_financial_data()\n",
        "\n",
        "# Save as CSV\n",
        "supplier_data.to_csv(\"supplier_data.csv\", index=False)\n",
        "procurement_orders.to_csv(\"procurement_orders.csv\", index=False)\n",
        "product_data.to_csv(\"product_data.csv\", index=False)\n",
        "logistics_data.to_csv(\"logistics_data.csv\", index=False)\n",
        "financial_data.to_csv(\"financial_data.csv\", index=False)\n",
        "\n",
        "# Download the files\n",
        "files.download(\"supplier_data.csv\")\n",
        "files.download(\"procurement_orders.csv\")\n",
        "files.download(\"product_data.csv\")\n",
        "files.download(\"logistics_data.csv\")\n",
        "files.download(\"financial_data.csv\")\n",
        "\n",
        "print(\"CSV files generated and ready for download!\")\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        },
        "id": "-dQA0FEn2LLk",
        "outputId": "71453a39-d899-4c3c-cea0-f04254146630"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_a5f0d751-dc07-4d4d-9367-6fee87f879eb\", \"supplier_data_extended.csv\", 68680)"
            ]
          },
          "metadata": {}
        }
      ]
    }
  ]
}