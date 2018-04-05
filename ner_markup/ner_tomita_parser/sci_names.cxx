#encoding "utf-8" 
#GRAMMAR_ROOT S 

 
//Define Names  
ProperName ->  Word<h-reg1>+; 

//Define scholar status
Status -> Noun<kwtype='scholar_status'>;

//Scholars' names could be found with their title before the name 
Scholar ->  (Adj<gnc-agr[1]>) (Status<gnc-agr[1]>) ProperName<gnc-agr[1], rt> (Status<gnc-agr[1]>); 

//Define actions going after the scholar's name
Action -> Verb<kwtype='scholar_action'> ;
Action_pres_sg -> Action<gram='praes, 3p, sg'> ;
Action_past_sg -> Action<gram='praet, 3p, sg'> | Action<gram='aor, 3p, sg'> ; //Uresolved past tense
Action_type -> Action_pres_sg | Action_past_sg ;


//Define affiliation

Abbreviation -> Word<h-reg2>+;
Location -> ProperName<gram='gen'> | 'в' ProperName<gram='abl'> | 
            Abbreviation<gram='gen'> | 'в' Abbreviation<gram='abl'> ;
            //Unresolved with abbreviations 

Institution -> 'из' (Adj<gnc-agr[1]>+) Noun<kwtype='institution', gram='gen', rt, gnc-agr[1]> 
             (Location+)  | 
            (Adj<gnc-agr[1]>+) Noun<kwtype='institution', gram='gen', rt, gnc-agr[1]>
            (Location+);

Affiliation -> Institution ;

S -> Scholar (Affiliation) (Action_type) ;
