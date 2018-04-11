#encoding "utf-8" 
#GRAMMAR_ROOT S 

 
//Define Names  
ProperName ->  Word<h-reg1>+ |  Word<h-reg1, gram='f'>+ ; 

//Define names with initials (abbreviated name)
Initial -> AnyWord<wff=/[А-ЯЁ]\./> ;
Initials -> Initial+ ;
AbrName ->  Word<h-reg1> Initials | Word<h-reg1, gram='f'> Initials |
            Initials  Word<h-reg1> | Initials Word<h-reg1, gram='f'> ;

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

//Define scholars plural contexts
Scholars_pl -> Scholar (Institution) 'и' Scholar (Institution) |
               (Adj<gnc-agr[1]>) Status<gram='pl', gnc-agr[1]> (Institution) ProperName 'и' ProperName|
               ProperName 'и' ProperName Action_type|
               Action_type ProperName 'и' ProperName|
               Citation_pl|
               ProperName 'и' ProperName Action_type Noun<gram='ins'>|
               Noun<gram='ins'> Action_type ProperName 'и' ProperName|
               Noun<gram='ins'> Action_type ProperName Scholar (Institution) 'и' Scholar (Institution)|
               Scholar (Institution) 'и' Scholar (Institution) Noun<gram='ins'> Action_type ;

//Define actions going after the scholar's name
Action -> Verb<kwtype='scholar_action'> ;
Action_pres_sg -> Action<gram='praes,sg'> ;
Action_past_sg -> Action<gram='praet,sg'> ;
Action_pres_pl -> Action<gram='praes,pl'> ;
Action_past_pl -> Action<gram='praet,pl'> ;
Action_type -> Action_pres_sg | Action_past_sg
               Action_pres_pl | Action_past_pl ;


//Define affiliation

Abbreviation -> Word<h-reg2>+; 
Location -> ProperName<gram='gen'> | 'в' ProperName<gram='abl'> ; 


Institution -> 'из' (Adj<gnc-agr[1]>+) Noun<kwtype='institution', gram='gen', rt, gnc-agr[1]> 
             (Location+)  | 
            (Adj<gnc-agr[1]>+) Noun<kwtype='institution', gram='gen', rt, gnc-agr[1]>
            (Location+)|
            Abbreviation;


//Define Pronouns
Pro -> Word<gram='SPRO'> ;

//Citation
Citation -> 'по' Noun<kwtype='citation', gram='dat,pl'> ProperName<gram='gen, sg'> (Institution) |
            'в' Noun<kwtype='citation', gram='abl,pl'> ProperName<gram='gen, sg'> (Institution) |
            Noun<kwtype='citation', gram='nom,sg'> ProperName<gram='gen,sg'> (Institution)|
            'в' Noun<kwtype='citation', gram='abl,sg'>  ProperName<gram='gen,sg'> (Institution)|

            //Unresolved with pro in citations
            ProperName 'в'(Pro) Noun<kwtype='citation', gram='abl,sg'> (Institution) |
            ProperName 'в' Noun<kwtype='citation', gram='abl,pl'> (Institution);

Citation_pl -> 'по' Noun<kwtype='citation', gram='dat,pl'> ProperName<gram='gen, sg'> (Institution) 
               'и' ProperName<gram='gen, sg'> (Institution) |
               'в' Noun<kwtype='citation', gram='abl,pl'> ProperName<gram='gen, sg'> (Institution) 'и'
               ProperName<gram='gen, sg'> (Institution)|
               Noun<kwtype='citation', gram='nom,sg'> ProperName<gram='gen,sg'> (Institution) 'и'
               ProperName<gram='gen, sg'> (Institution)|
               'в' Noun<kwtype='citation', gram='abl,sg'>  ProperName<gram='gen,sg'> (Institution) 'и'
               ProperName<gram='gen, sg'> (Institution)|
               ProperName 'и' ProperName 'в' Noun<kwtype='citation', gram='abl,sg'> (Institution) |
               ProperName 'и' ProperName 'в' Noun<kwtype='citation', gram='abl,pl'> (Institution);

//S -> Scholar (Institution) (Action_type) | Scholars_pl (Institution) (Action_type) ;
S -> AbrName;