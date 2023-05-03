{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN+QE64keXAOZ96HXdQQPVW",
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
        "<a href=\"https://colab.research.google.com/github/hyeontae04/202310968/blob/main/hw7.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "tUyHWMsMHTjc"
      },
      "outputs": [],
      "source": [
        "len(d) = {'banana':'바나나','apple':'사과'}\n",
        "len(d)[''] = ''\n",
        "shopping_bag = [] #장바구니\n",
        "print('[구입]')\n",
        "while True:\n",
        "  item = input('상품명?')\n",
        "  if item == '':\n",
        "    break\n",
        "  shopping_bag.append(item)\n",
        "  print(f'장바구니에 {item}가(이) 담겼습니다.Wn')\n",
        "  len(d) = input('수량은?')\n",
        "  if len(d) == ''\n",
        "  break\n",
        "\n",
        "print(f'Wn>>> 장바구니 보기:{shopping_bag}')\n",
        "print('[검색]')\n",
        "print('장바구니에서 확인하고자 하는 상품은?', item)\n",
        "print(f'{item}은(는) {len(d)}개 담겨 있습니다.')\n"
      ]
    }
  ]
}