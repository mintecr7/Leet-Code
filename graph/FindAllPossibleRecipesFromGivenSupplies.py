from typing import List 


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

      can_make = []
      put = False
      # for i in ingredients[0]:
      #   print(i)
      for idx, recipe in enumerate(recipes):
   
        for ingredient in ingredients[idx]:
          if ingredient in supplies or ingredient in can_make:
            if not put:
              put = True
            continue
          else:
            put = False
            break 
        if put:
          can_make.append(recipe)

      return can_make





supplies = ["yeast","flour","meat"]
recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]


a = Solution()

ans = a.findAllRecipes(
   recipes=recipes,
   ingredients=ingredients,
   supplies=supplies
)

print(ans)