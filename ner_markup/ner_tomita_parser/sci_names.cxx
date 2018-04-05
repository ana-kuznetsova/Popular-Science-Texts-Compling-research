#encoding "utf-8" 
#GRAMMAR_ROOT S 

 
//Define Names  
ProperName ->  Word<h-reg1>+; 
//Scholars' names could be found with their title before the name 
Scholar ->  (Adj<gnc-agr[1]>) (Noun<kwtype='статус_ученых', gnc-agr[1]>) ProperName<gnc-agr[1], rt>; 

//Define actions going after the scholar's name
Action -> Verb<kwtype='действия_ученых'> ;
Action_pres_sg -> Action<gram='praes, 3p, sg'> ;
Action_past_sg -> Action<gram='praet, 3p, sg'> ; //Uresolved past tense
Action_type -> Action_pres_sg | Action_past_sg ;

S -> Scholar Action_type ;
