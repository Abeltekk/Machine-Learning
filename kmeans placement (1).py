{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0      1\n",
      "1      1\n",
      "2      1\n",
      "3      1\n",
      "4      1\n",
      "      ..\n",
      "210    1\n",
      "211    1\n",
      "212    1\n",
      "213    0\n",
      "214    1\n",
      "Name: gender, Length: 215, dtype: int64\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYIAAAEWCAYAAABrDZDcAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAc8UlEQVR4nO3df5wcdZ3n8dd7Jg32ADoBZiEMGbJwGm8hhMBIgniud6hRlh8Bg4QHUfDksire6q2b9ccDFXjAsmd28XBBvAisAYFVEWLwcLO4/kB2JTJJgGyAKAYkv4SBOPzKaIbJ5/6omqSn0z3TE6amM13v5+Mxj+mu+ta3PtU10++uH12liMDMzPKrqd4FmJlZfTkIzMxyzkFgZpZzDgIzs5xzEJiZ5ZyDwMws5xwE1hAkhaT/VO86zMYjB4GNOUn7SrpR0m8kvSRptaT3DjPNpHSaLek0j0u6TNJ+o1jXNyRdMVr9VepT0tHpMnyqSvsr0lD7WNnwv0qHXzKa9ZmBg8DqYwKwAfhT4A3A54FvS5pSqbGkA4GfA0XgpIg4AHgX0AocNQb11kTShGHGHwf8GLgyIv5+iKa/BC4oG/aBdLjZqHMQ2JiLiFci4tKIeCoidkTE94EngROqTPKXwEvA/Ih4Ku1jQ0R8IiIeKW8s6SeSLip5fqGk+9PHkvRlSc9KekHSI5KOkbQAOB/4a0kvS7o7bX+YpO9K6pb0pKS/KOn3Ukl3SPqmpBeBC6sts6QTgR8Cn4uIa4d5iX4OHChpajrtcST/q6vL+jxD0sOSeiTdL+mYknGXSFqfbj2tlXRGybiLJP00fR160nbvLhn/YUlPpdOulzRvmHptnHMQWN1JOgR4E7C2SpN3AndGxI5RmN27gben82sFzgWej4jFwK3AlyJi/4g4XVITcDfwMNAOnAJ8UtLskv7OBO5I+7q1yjxPBP4Z+F8RcUONdd4CfDB9/EHg5tKRkt4CfB24CDgIuAn4nqR90ia/BE4m2eK6ErgtfZ0HvBVYk077ZeDGtN/XA1cD70q3vE4GdgtbaywOAqsrSQWSN9AlEfF4lWYHAVtGaZZ9wAHAmwFFxGMRUa3vtwBtEXF5RGyPiPUkb76ln5B/HhFL0y2b3ir9zAJeAH4wgjpvAc5PX5/3s3vILAC+GhEPRkR/RNxUUjMR8e2I2JLWdRvwFNBZMv2vI+KmiOgHlgCHSzo4HRfAMZJel/bx6AjqtnHIQWB1k37ivgXYDnx8iKbPA5NGY54R8SPgWuA64BlJi9NPwZUcARyW7j7pkdQDfA4o/WS9oYbZXgc8CNwraeLAQEkXpLuhdu6KKqnzSeBp4G+AtRGxuUJtny6rbRLJlsvA7rCHS8a9GTi4ZPrfljzelv7ePyJeBM4DLgZ+K+n7kt5UwzLaOOYgsLqQJJLdEYcA74uIviGa/xA4Kw2OWrwCtJQ8P7R0ZER8JSJOAI4m2UW0cGBUWT8bgCcjorXk54CIOLW0uxrq6Sc5/vA0sHwgeCJiSbobav+IOL3CdDcDn6Jst1BJbZeV1dYSEd+WdCRwPfBR4KCIaAUeB1RDrUTEDyLinSTB8gTwf2uZzsYvB4HVy/XAfwZOH2KXyoCrgdcDSyQdASCpXdLVko6t0P4h4GxJLel3Cz48MELSWyTNTHe5vAL8nuSNGuAZ4MiSfn4BvCjp05KKkprTA8tvGenCpkF3DvAccE+Np73eRnJM47sVxi0GLk6XR5L2l3R62u/+JAHVnSyyLiLZIhiWktN0T5fUQrKl9gq7Xh9rUA4CG3Ppm/mfA8eR7H4Y2D1yfqX2EbGV5OBmH7BC0kvAv5Lsd3+iwiRfJnkTe4Zk/3fp/vXXk+zn/x3wG5LdTn+XjrsR+JN0d8rSdP/56WmdT5K8id9AcgB2xCJiO3A2SfjcLak4TPttEfHDiPh9hXErSD7xX58uyy+B+em4R4CvkATZFpIQWFFjmc0kW0hbSF6btzL0bjtrAPKNaczM8s1bBGZmOecgMDPLOQeBmVnOOQjMzHJuyItk7Y0OPvjgmDJlSr3LMDMbV1auXPlcRLRVGjfugmDKlCl0dXXVuwwzs3FF0m+qjfOuITOznHMQmJnlnIPAzCznHARmZjnnIDAzyzkHgZlZzmV2+qik1wH3Afum87kjIr5Y1mZfkmutn0BypcNzB+5JO9ouWbqG21dsoL/kInvNEv0RtLcWWTh7KnNmtAOwdPUmFi1fx6ae3p1tWosFevv6+cOru+6WuN8+zZx1fDv/75Et/G5b5cvpT2wp8GfHTuLHj3ezuaeXw9J5AVy6bC09vbumE7Vd3F7AW486kKee72VzTy8t+zTzyvZdVwoeqOuuVZsGDd9TE1sKfPH0o3e+PmbWWDK7+mh645H9IuLl9Nrv9wOfiIgHStp8DDg2Ij6S3iD7rIg4d6h+Ozs7Y6TfI7hk6Rq++cDTQ7YpFpq56uxpAHz2zjX09mV3CfZCUxIuO8bRhV8LzWLR3OkOA7NxStLKiOisNC6zXUOReDl9Wkh/yt/6ziS5XjwkNwA/JQ2QUXX7iuHvJtjb18+i5etYtHxdpiEA0LdjfIUAQF9/sGj5unqXYWYZyPQYQXpHp4eAZ4F705tplGonvedrRLxKcqORgyr0s0BSl6Su7u7uEdfRX+NWz+aeZFeLVebXxqwxZRoEEdEfEccBhwMnSjqmrEmlT/+7vWtHxOKI6IyIzra2ipfKGFJzjRsZh7UWOax1yJtG5ZpfG7PGNCZnDUVED/AT4D1lozYCkwEkTSC5BeDW0Z7/eTMnD9umWGhm4eypLJw9lWKhebRLGKTQJJpGfQdYtgrN2nmQ28waS2ZBIKlNUmv6uAi8E3i8rNky4IL08VzgR5HB0esr5kxj/qyO3bYMBp63txa56uxpzJnRzpwZ7Vx19jTa00+/A21aiwX2nTD45dpvn2bmz+pgYkuh6rwnthSYP6uD9tYiSue16JzpXP3+42gtDp6u1mwQcPJRB+7sc799BgfXQF3lw/fUxJaCDxSbNbAszxo6luRAcDNJ4Hw7Ii6XdDnQFRHL0lNMbwFmkGwJzIuI9UP1uydnDZmZ5d1QZw1l9j2CiHiE5A2+fPgXSh7/HjgnqxrMzGx4/maxmVnOOQjMzHLOQWBmlnMOAjOznHMQmJnlnIPAzCznHARmZjnnIDAzyzkHgZlZzjkIzMxyzkFgZpZzDgIzs5xzEJiZ5ZyDwMws5xwEZmY55yAwM8s5B4GZWc45CMzMcs5BYGaWcw4CM7OccxCYmeWcg8DMLOccBGZmOecgMDPLucyCQNJkST+W9JiktZI+UaHNOyS9IOmh9OcLWdVjZmaVTciw71eBT0XEKkkHACsl3RsRj5a1+1lEnJZhHWZmNoTMtggiYktErEofvwQ8BrRnNT8zM9szY3KMQNIUYAawosLokyQ9LOkHko6uMv0CSV2Surq7uzOs1MwsfzIPAkn7A98FPhkRL5aNXgUcERHTgX8AllbqIyIWR0RnRHS2tbVlW7CZWc5kGgSSCiQhcGtE3Fk+PiJejIiX08f3AAVJB2dZk5mZDZblWUMCbgQei4irq7Q5NG2HpBPTep7PqiYzM9tdlmcNnQx8AFgj6aF02OeADoCI+BowF/iopFeBXmBeRESGNZmZWZnMgiAi7gc0TJtrgWuzqsHMzIbnbxabmeWcg8DMLOccBGZmOecgMDPLOQeBmVnOOQjMzHLOQWBmlnMOAjOznHMQmJnlnIPAzCznHARmZjnnIDAzyzkHgZlZzjkIzMxyzkFgZpZzDgIzs5xzEJiZ5ZyDwMws5xwEZmY55yAwM8s5B4GZWc45CMzMcs5BYGaWcxOy6ljSZOBm4FBgB7A4Iq4payPgGuBUYBtwYUSsyqomMxuZpas3sWj5Ojb39HJYa5EpBxX5t19v3TlewPmzOug84sCd7d5QLCBBz7a+ndM8sP539EcM6ru1WOC06ZO4c+VGtvXt2G3ezRL9Ebv9bm8tsnD2VIBBtS2cPZU5M9oH1b2pp7fm6Zau3sRld6/ld9v6dtZ36RlH7+yz1tdoYB6XLltLT2/S18SWAl88ffi+RjKPPe2rEkXZyhm1jqVJwKSIWCXpAGAlMCciHi1pcyrwP0mCYCZwTUTMHKrfzs7O6OrqyqRmM9tl6epNfPbONfT29Q/btkmwI5u3kooKzYKAvpKZFgvNXHX2NICqdVeb7n0ntPOtBzfQ1z94IQpNYtE506u+6VZ6jQrNor8/KI+2QrNYNLd6X9VUmsfAso6kL0krI6Kz0rjMdg1FxJaBT/cR8RLwGFBe9ZnAzZF4AGhNA8TM6mzR8nU1hQCMbQgA9PXHoDdzgN6+fhYtXzdk3dWmu33F7iEASWAsWr6uah2V5tVXIQQGhg/V10jmMbCsoyWzXUOlJE0BZgAryka1AxtKnm9Mh20pm34BsACgo6MjqzLNrMTmnt56lzBie1pz+W6rWvsc6fz2pL5q04zm+sn8YLGk/YHvAp+MiBfLR1eYZLc1EhGLI6IzIjrb2tqyKNPMyhzWWqx3CSN2WGtxj+puVqW3ol197sm40Wg/1DSjuX4yDQJJBZIQuDUi7qzQZCMwueT54cDmLGsys9osnD2VYqG5prZN1d9HM1FoFoWymRYLzSycPXXIuqtNd97Mycnxg/L2Tdp58LeSSvMqNKviG2uheei+RjKPgWUdLZkFQXpG0I3AYxFxdZVmy4APKjELeCEitlRpa2ZjaM6Mdq46exrtrUUEtLcWOfmoAwe1ETB/VgdXv/+4ne1aiwUmthQGTVPpE3drscD8WR20FCq/DQ1MU/67vbXIornTWXTO9EG1DRw8La271umumDONRXOnM7GlMKi+oQ4UV3uNFs2dztXnHkdrcVdfE1sKe3SguNo8RnqgeDhZnjX0NuBnwBrYeezkc0AHQER8LQ2La4H3kJw++qGIGPKUIJ81ZGY2ckOdNZTZweKIuJ/KxwBK2wRwcVY1mJnZ8PzNYjOznHMQmJnlnIPAzCznHARmZjnnIDAzyzkHgZlZzjkIzMxyzkFgZpZzDgIzs5xzEJiZ5ZyDwMws5xwEZmY55yAwM8u5moJAUoukz0v6evr8jZJOy7Y0MzMbC7VuEfwj8AfgpPT5RuCKTCoyM7MxVWsQHBURXwL6ACKil2HuNWBmZuNDrUGwXVKR9Mbyko4i2UIwM7NxrtY7lH0R+GdgsqRbgZOBC7MqyszMxk5NQRAR90paBcwi2SX0iYh4LtPKzMxsTNR61pCA9wInRMT3gRZJJ2ZamZmZjYlajxF8leSMofPS5y8B12VSkZmZjalajxHMjIjjJa0GiIjfSdonw7rMzGyM1LpF0CepmV1nDbUBOzKryszMxkytQfAV4C7gjyRdCdwP/E1mVZmZ2Zip9ayhWyWtBE4hOWtoTkQ8NtQ0km4CTgOejYhjKox/B/A94Ml00J0RcfkIajczs1EwbBBIagIeSd/MHx9B398ArgVuHqLNzyLC1ywyM6ujYXcNRcQO4GFJHSPpOCLuA7buaWFmZjY2aj1raBKwVtIvgFcGBkbEGa9x/idJehjYDPxVRKyt1EjSAmABQEfHiPLIzMyGUWsQXJbBvFcBR0TEy5JOBZYCb6zUMCIWA4sBOjs7I4NazMxyq9aDxT8d7RlHxIslj++R9FVJB/vSFWZmY6vWS0y8JOnFsp8Nku6SdOSezFjSoemlK0gvV9EEPL8nfZmZ2Z6rddfQ1ST78W8jOX10HnAosA64CXhH+QSSbk+HHyxpI8kVTAsAEfE1YC7wUUmvAr3AvIjwbh8zszGmWt57Ja2IiJllwx6IiFmSHo6I6ZlVWKazszO6urrGanZmZg1B0sqI6Kw0rtZvFu+Q9H5JTenP+0vG+VO8mdk4VmsQnA98AHgWeCZ9PD+9a9nHM6rNzMzGQK1nDa0HTq8y+v7RK8fMzMZarWcNvUnSv0r6j/T5sZIuybY0MzMbC7XuGvo68FmgDyAiHiE5c8jMzMa5WoOgJSJ+UTbs1dEuxszMxl6tQfCcpKPYdWOaucCWzKoyM7MxU+sXyi4mudbPmyVtIrmHwPmZVWVmZmNmyCCQ9JclT+8BfkyyFfEK8D6Sbxybmdk4NtwWwQHp76nAW0juKCaS7xHcl2FdZmY2RoYMgoi4DEDSvwDHR8RL6fNLge9kXp2ZmWWu1oPFHcD2kufbgSmjXo2ZmY25Wg8W3wL8QtJdJGcOnQUsyawqMzMbM7VeYuJKST8A/ks66EMRsTq7sszMbKzUukVARKwiub2kmZk1kFqPEZiZWYNyEJiZ5ZyDwMws5xwEZmY55yAwM8s5B4GZWc45CMzMcs5BYGaWcw4CM7Ocq/mbxSMl6SbgNODZiDimwngB1wCnAtuAC9NvL9teYunqTSxavo7NPb1MaIK+HfWuqLKWQhPb+nYg0lvovQZNgh0B7a1FFs6eypwZ7aNRotleLcstgm8A7xli/HuBN6Y/C4DrM6zFRmjp6k189s41bOrpJdh7QwBgW1rcaw0BSEIAYFNPL5+9cw1LV28ahV7N9m6ZBUFE3AdsHaLJmcDNkXgAaJU0Kat6bGQWLV9Hb19/vcuoq96+fhYtX1fvMswyV89jBO3AhpLnG9Nhu5G0QFKXpK7u7u4xKS7vNvf01ruEvYJfB8uDegaBKgyruHUfEYsjojMiOtva2jIuywAOay3Wu4S9gl8Hy4N6BsFGYHLJ88OBzXWqxcosnD2VYqG53mXUVbHQzMLZU+tdhlnm6hkEy4APKjELeCEittSxHisxZ0Y7V509jfbWIgIKe/GJxi1pcZU2MUeqKe2kvbXIVWdP81lDlgtZnj56O/AO4GBJG4EvAgWAiPgacA/JqaNPkJw++qGsarE9M2dGu98IzXIgsyCIiPOGGR/AxVnN38zMarMXb/CbmdlYcBCYmeWcg8DMLOccBGZmOecgMDPLOQeBmVnOOQjMzHLOQWBmlnMOAjOznHMQmJnlnIPAzCznHARmZjnnIDAzyzkHgZlZzjkIzMxyzkFgZpZzDgIzs5xzEJiZ5ZyDwMws5xwEZmY55yAwM8s5B4GZWc45CMzMci7TIJD0HknrJD0h6TMVxl8oqVvSQ+nPRVnWY2Zmu5uQVceSmoHrgHcBG4EHJS2LiEfLmn4rIj6eVR1mZja0LLcITgSeiIj1EbEd+CfgzAznZ2ZmeyDLIGgHNpQ835gOK/c+SY9IukPS5EodSVogqUtSV3d3dxa1mpnlVpZBoArDouz53cCUiDgW+CGwpFJHEbE4IjojorOtrW2UyzQzy7csg2AjUPoJ/3Bgc2mDiHg+Iv6QPv06cEKG9ZiZWQVZBsGDwBsl/bGkfYB5wLLSBpImlTw9A3gsw3rMzKyCzM4aiohXJX0cWA40AzdFxFpJlwNdEbEM+AtJZwCvAluBC7Oqx8zMKlNE+W77vVtnZ2d0dXXVuwwzs3FF0sqI6Kw0zt8sNjPLOQeBmVnOOQjMzHLOQWBmlnMOAjOznHMQmJnlnIPAzCznHARmZjnnIDAzyzkHgZlZzjkIzMxyzkFgZpZzDgIzs5xzEJiZ5ZyDwMws5xwEZmY55yAwM8s5B4GZWc45CMzMcs5BYGaWcw4CM7OccxCYmeWcg8DMLOccBGZmOTchy84lvQe4BmgGboiIvy0bvy9wM3AC8DxwbkQ8lWVNZrW6ZOkablvxNDsieV4sNHF8Ryv//uutRIX2+zSL5ibR27djt3GFJugPdvaVldZigdOmT+LHj3ezuaeXw1qLTDmoyL/9euugdi2FJmZ0tPLz9Vt3q6ml0ETvqzuIgGaJ82ZO5oo507It3OpKEdn8ZUpqBn4JvAvYCDwInBcRj5a0+RhwbER8RNI84KyIOHeofjs7O6OrqyuTms0GXLJ0Dd984Ol6l7HXmD+rw2EwzklaGRGdlcZluWvoROCJiFgfEduBfwLOLGtzJrAkfXwHcIokZViTWU1uX7Gh3iXsVfx6NLYsg6AdKP3r2ZgOq9gmIl4FXgAOKu9I0gJJXZK6uru7MyrXbJf+jLaUxyu/Ho0tyyCo9Mm+/K+pljZExOKI6IyIzra2tlEpzmwozd4wHcSvR2PLMgg2ApNLnh8ObK7WRtIE4A3AVszq7LyZk4dvlCN+PRpblkHwIPBGSX8saR9gHrCsrM0y4IL08VzgR5HV0WuzEbhizjTmz+qgqeSDcLHQxMlHHVhxMxaSs4aKhcr/UoUmBvWVldZigfmzOmhvLSKgvbXIyUcduFu7lnRZKtXUUmhiYAOgWfKB4hzI7KwhAEmnAv+H5PTRmyLiSkmXA10RsUzS64BbgBkkWwLzImL9UH36rCEzs5Eb6qyhTL9HEBH3APeUDftCyePfA+dkWYOZmQ3N3yw2M8s5B4GZWc45CMzMcs5BYGaWcw4CM7Ocy/T00SxI6gZ+AxwMPFfncrLmZWwMXsbGMN6X8YiIqHhphnEXBAMkdVU7J7ZReBkbg5exMTTyMnrXkJlZzjkIzMxybjwHweJ6FzAGvIyNwcvYGBp2GcftMQIzMxsd43mLwMzMRoGDwMws58ZFEEh6StIaSQ9J6kqHHSjpXkm/Sn9PrHedr0WVZbxU0qZ02EPpZb3HLUmtku6Q9LikxySd1IDrsdIyNsx6lDS1ZDkekvSipE820nocYhkbZj2WGxfHCCQ9BXRGxHMlw74EbI2Iv5X0GWBiRHy6XjW+VlWW8VLg5Yj4u3rVNZokLQF+FhE3pDcragE+R2Otx0rL+EkaaD0OkNQMbAJmAhfTQOtxQNkyfogGXI8wTrYIqjgTWJI+XgLMqWMtNgxJrwfeDtwIEBHbI6KHBlqPQyxjozoF+HVE/IYGWo9lSpexYY2XIAjgXyStlLQgHXZIRGwBSH//Ud2qGx2VlhHg45IekXTTeN7cBo4EuoF/lLRa0g2S9qOx1mO1ZYTGWY+l5gG3p48baT2WKl1GaMz1OG6C4OSIOB54L3CxpLfXu6AMVFrG64GjgOOALcDf17G+12oCcDxwfUTMAF4BPlPfkkZdtWVspPUIQLrb6wzgO/WuJSsVlrHh1uOAcREEEbE5/f0scBdwIvCMpEkA6e9n61fha1dpGSPimYjoj4gdwNdJlnu82ghsjIgV6fM7SN40G2k9VlzGBluPA94LrIqIZ9LnjbQeBwxaxgZdj8A4CAJJ+0k6YOAx8G7gP4BlwAVpswuA79Wnwteu2jIO/GOlziJZ7nEpIn4LbJA0NR10CvAoDbQeqy1jI63HEucxeJdJw6zHEoOWsUHXIzAOzhqSdCTJJ2RINr1vi4grJR0EfBvoAJ4GzomIrXUq8zUZYhlvIdkMDeAp4M8H9sOOR5KOA24A9gHWk5yF0USDrEeouoxfobHWYwuwATgyIl5IhzXM/yNUXcaG+n8stdcHgZmZZWuv3zVkZmbZchCYmeWcg8DMLOccBGZmOecgMDPLOQeBWYYkfUPS3HrXYTYUB4HZXkTShHrXYPnjPzqzlKTPA+eTfJHoOWAlyRf9rgPagG3A/4iIxyV9A3gR6AQOBf46Iu6QJOAfgP8GPAmopP8TgKuB/dP+L4yILZJ+Avw7cDLJN3Qb5ho2Nj44CMwASZ3A+4AZJP8Xq0iCYDHwkYj4laSZwFdJ3uQBJgFvA95M8gZ+B8mlB6YC04BDSC6jcZOkAklAnBkR3ZLOBa4E/nvaV2tE/GnmC2pWgYPALPE24HsR0Qsg6W7gdcBbge8kH/QB2LdkmqXpBcgelXRIOuztwO0R0Q9slvSjdPhU4Bjg3rSvZpIrWA741ugvklltHARmCVUY1gT0RMRxVab5Q5XpK123RcDaiDipSl+vDF+iWTZ8sNgscT9wuqTXSdof+DOSYwJPSjoHQInpw/RzHzBPUnN6tcr/mg5fB7RJOintqyDp6EyWxGyEHARmQEQ8SLKf/2HgTqALeIHk4PGHJT0MrCW5JeNQ7gJ+BawhuZHJT9P+twNzgf+d9vUQyW4ns7rz1UfNUpL2j4iX00sQ3wcsiIhV9a7LLGs+RmC2y2JJf0JykHiJQ8DywlsEZmY552MEZmY55yAwM8s5B4GZWc45CMzMcs5BYGaWc/8f7sjEVv2bnaMAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas\n",
    "import pylab as pl\n",
    "from sklearn.cluster import KMeans\n",
    "from sklearn.decomposition import PCA\n",
    "from sklearn import preprocessing\n",
    "\n",
    "le = preprocessing.LabelEncoder()\n",
    "\n",
    "variables = pandas.read_csv('Placement.csv')\n",
    "variables.gender = le.fit_transform(list(variables[\"gender\"]))\n",
    "print (variables.gender)\n",
    "X = variables[['gender']]\n",
    "Y = variables[['mba_p']]\n",
    "\n",
    "\n",
    "kmeans=KMeans(n_clusters=4)\n",
    "kmeansoutput=kmeans.fit(Y)\n",
    "y_km=kmeansoutput.labels_\n",
    "\n",
    "pl.scatter(Y, y_km)\n",
    "pl.xlabel('gender')\n",
    "pl.ylabel('degree')\n",
    "pl.title('2 Cluster K-Means')\n",
    "pl.show()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
