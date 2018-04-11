#encoding "utf-8" 
#GRAMMAR_ROOT S 

 
//Define Names  
ProperName ->  Word<h-reg1>+ |  Word<h-reg1, gram='f'>+ ; 

//Define scholar status
Status -> Noun<kwtype='scholar_status'>;

//Scholars' names could be found with their title before the name 

Scholar ->  (Adj<gnc-agr[1]>) Status<gnc-agr[1]> ProperName<gnc-agr[1], rt> |
            (Adj<gnc-agr[1]>) ProperName<gnc-agr[1], rt> Status<gnc-agr[1]> |           
            Citation |
            ProperName Action_type |
            //feminitive agreement
             (Adj<fem-c-agr[1]>) Status<fem-c-agr[1]> ProperName<fem-c-agr[1], rt>| 
             (Adj<fem-c-agr[1]>) ProperName<fem-c-agr[1], rt> Status<fem-c-agr[1]>
            ; 

//Define actions going after the scholar's name
Action -> Verb<kwtype='scholar_action'> ;
Action_pres_sg -> Action<gram='praes,3p,sg'> ;
Action_past_sg -> Action<gram='praet,sg'> ;
Action_type -> Action_pres_sg | Action_past_sg ;


//Define affiliation

Abbreviation -> Word<h-reg2>+; 
Location -> ProperName<gram='gen'> | 'в' ProperName<gram='abl'> ; 


Institution -> 'из' (Adj<gnc-agr[1]>+) Noun<kwtype='institution', gram='gen', rt, gnc-agr[1]> 
             (Location+)  | 
            (Adj<gnc-agr[1]>+) Noun<kwtype='institution', gram='gen', rt, gnc-agr[1]>
            (Location+)|
            Abbreviation;


//Citation
Citation -> 'по' Noun<kwtype='citation', gram='dat,pl'> ProperName<gram='gen, sg'> (Institution) |
            'в' Noun<kwtype='citation', gram='abl,pl'> ProperName<gram='gen, sg'> (Institution) |
            Noun<kwtype='citation', gram='nom,sg'> ProperName<gram='gen,sg'> (Institution)|
            'в' Noun<kwtype='citation', gram='abl,sg'>  ProperName<gram='gen,sg'> (Institution)|
            ProperName 'в' Noun<kwtype='citation', gram='abl,sg'> (Institution) ;



S -> Scholar (Institution) (Action_type);
