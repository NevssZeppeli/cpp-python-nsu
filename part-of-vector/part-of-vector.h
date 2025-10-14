#pragma once

#include <vector>
#include <iostream>
#include <iterator>

void PrintVectorPart(const std::vector<int>& v, std::ostream& os = std::cout) {
   // unsigned int neg_index = v.size(); 
   //  for (unsigned int i = 0; i < v.size(); i++) { // компилятор ругался, что сравнивать unsigned и обычную переменную - нехорошо
   //      if (v[i] < 0) {
   //          neg_index = i;
   //          break;
   //      }
   //  }

   // for (unsigned int i = 0; i < neg_index; i++) {
   //    if (i > 0) {
   //       os << " ";
   //    }
   //    os << v[neg_index - 1 - i];
   // }

   // в один цикл
   // unsigned int i = 0;
   // if (v.empty()) return;

   // while (i < v.size() && v[i] >= 0) {
   //    i++;
   // }

   // if (i == 0) return;
   // unsigned int j = i - 1;
   
   // os << v[j];
   // while (j > 0) {
   //    j--;
   //    os << " " << v[j];
   // }

   unsigned int i = 0;
   unsigned int neg_index = 0;
   bool found = false;
   bool first = true;

   while (true) {
         if (!found) {
            if (i < v.size() && v[i] >= 0) {
               i++;
               continue;
         }
         neg_index = i;
         if (neg_index == 0) return;
         i = neg_index - 1;
         found = true;
         continue;
       
      if (!first) os << " ";
      os << v[i];
      first = false;
      if (i == 0) break;
      i--;
}
}
