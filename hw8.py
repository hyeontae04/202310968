{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOOrNYhm7Zo3r+h/oAXdY0s",
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
        "<a href=\"https://colab.research.google.com/github/hyeontae04/202310968/blob/main/hw8.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nei-5qJoex6Y",
        "outputId": "4e33f27a-d1d5-444a-8292-d7fadf68a427"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[구입]\n",
            "상품명?샌드위치\n",
            "수량은?10\n",
            "장바구니에 샌드위치 10개가 담겼습니다.\n",
            "상품명?주스\n",
            "수량은?5\n",
            "장바구니에 주스 5개가 담겼습니다.\n",
            "상품명?\n",
            "[Wn구입]\n",
            "상품명?주스\n",
            ">>> 장바구니 보기:[10, '샌드위치', 5, '주스']:5\n",
            "Wn[검색]\n",
            "장바구니에서 확인하고자 하는 상품은?주스\n",
            "3(는) 5개 담겨 있습니다.\n"
          ]
        }
      ],
      "source": [
        "shopping_bag = [] #장바구니\n",
        "print('[구입]')\n",
        "while True:\n",
        "  item = input('상품명?')\n",
        "  if item == '': #빈 문자열이면 루프 탈출\n",
        "    break\n",
        "  nums = int(input('수량은?'))\n",
        "  if nums == '': #빈 정수형이면 루프 탈출\n",
        "    break\n",
        "  shopping_bag.append(nums) \n",
        "  shopping_bag.append(item)\n",
        "  print(f'장바구니에 {item} {nums}개가 담겼습니다.')\n",
        "\n",
        "print('[Wn구입]')\n",
        "item = input('상품명?')\n",
        "print(f'>>> 장바구니 보기:{shopping_bag}:{nums}')\n",
        "\n",
        "print('Wn[검색]')\n",
        "item = input('장바구니에서 확인하고자 하는 상품은?')\n",
        "if item in shopping_bag:\n",
        "  item = shopping_bag.index(item)\n",
        "  print(f'{item}(는) {nums}개 담겨 있습니다.')\n",
        "else:\n",
        "  print(f'장바구니에 {item}은(는) 없습니다.')"
      ]
    }
  ]
}