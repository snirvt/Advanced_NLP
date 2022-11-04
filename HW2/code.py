{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOGDdfXBqJmrhpie2WVGs/B",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/snirvt/Advanced_NLP/blob/main/HW2/code.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iQSc7m3MR2UP",
        "outputId": "80855959-b897-4779-f6ba-6f7e3e64492d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: destination path 'spider_execution_plans' already exists and is not an empty directory.\n"
          ]
        }
      ],
      "source": [
        "! git clone https://github.com/beneyal/spider_execution_plans"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "! ls -la"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9uHf8glZR51K",
        "outputId": "f551d511-6706-46af-9689-6c3f40849bf1"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "total 20\n",
            "drwxr-xr-x 1 root root 4096 Nov  4 15:34 .\n",
            "drwxr-xr-x 1 root root 4096 Nov  4 15:33 ..\n",
            "drwxr-xr-x 4 root root 4096 Nov  2 13:38 .config\n",
            "drwxr-xr-x 1 root root 4096 Nov  2 13:40 sample_data\n",
            "drwxr-xr-x 5 root root 4096 Nov  4 15:34 spider_execution_plans\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "! pip install typing\n",
        "# from typing import Literal, Tuple"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0j8c_e36Y3RI",
        "outputId": "cef4a5be-6aad-4dd6-ca45-f04b12915e69"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: typing in /usr/local/lib/python3.7/dist-packages (3.7.4.3)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ! pip install -r requirements.txt"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a_LaWwQ3SAGU",
        "outputId": "5f357751-08d9-4aac-aeb5-e4e1187fb6c3"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[31mERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from spider_execution_plans.spider_execution_plans.execution_plans.ep_reader import get_train_dev_spider_instances"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 444
        },
        "id": "5PmgatomSfoY",
        "outputId": "7666626f-bec4-4667-d434-2dd622c87c13"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ImportError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-3-044cedf739ce>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mspider_execution_plans\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mspider_execution_plans\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecution_plans\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mep_reader\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mget_train_dev_spider_instances\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/content/spider_execution_plans/spider_execution_plans/execution_plans/ep_reader.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mdataclasses\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mdataclass\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mtyping\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mLiteral\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mTuple\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mlxml\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0metree\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mImportError\u001b[0m: cannot import name 'Literal' from 'typing' (/usr/lib/python3.7/typing.py)",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "zUxRGeLrYwt8"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}