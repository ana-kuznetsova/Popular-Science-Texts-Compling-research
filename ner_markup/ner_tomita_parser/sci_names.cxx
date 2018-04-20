#encoding "utf-8" 
#GRAMMAR_ROOT S 

 
//Define Names  
ProperName ->  Word<~fw, h-reg1>+ |  Word<~fw, h-reg1, gram='f'>+ ; 

//Define names with initials (abbreviated name)
Initial -> AnyWord<wff=/[А-ЯЁ]\./> ;
Initials -> Initial+ ;
AbrName ->  Word<h-reg1> Initials | Word<h-reg1, gram='f'> Initials |
            Initials  Word<h-reg1> | Initials Word<h-reg1, gram='f'> ;

//Define scholar status
Status -> Noun<kwtype='scholar_status'>;

//Define Scholar non-terminal

Scholar ->  (Adj<gnc-agr[1]>) Status<gnc-agr[1], gram='sg'> ProperName<gnc-agr[1], rt> |
            (Adj<gnc-agr[1]>) ProperName<gnc-agr[1], rt> Status<gnc-agr[1], gram='sg'> |           
            Citation |
            ProperName Action_type |
            //feminitive agreement with ProperName
             (Adj<fem-c-agr[1]>) Status<fem-c-agr[1], gram='sg'> ProperName<fem-c-agr[1], rt>| 
             (Adj<fem-c-agr[1]>) ProperName<fem-c-agr[1], rt> Status<fem-c-agr[1], gram='sg'>|
             //Abbreviated names 
            (Adj<gnc-agr[1]>) Status<gnc-agr[1], gram='sg'> AbrName<gnc-agr[1], rt> |
            (Adj<gnc-agr[1]>) AbrName<gnc-agr[1], rt> Status<gnc-agr[1], gram='sg'> |
            //Abbreviated fem names
            (Adj<fem-c-agr[1]>) Status<fem-c-agr[1], gram='sg'> AbrName<fem-c-agr[1], rt>| 
            (Adj<fem-c-agr[1]>) AbrName<fem-c-agr[1], rt> Status<fem-c-agr[1], gram='sg'>
            ; 

//Define scholars plural contexts
Scholars_pl -> Scholar (Institution) 'и' Scholar (Institution) |
               (Adj<gnc-agr[1]>) Status<gram='pl', gnc-agr[1]> (Institution) ProperName 'и' ProperName|
               ProperName 'и' ProperName Action_type|
               Action_type ProperName 'и' ProperName|
               Citation_pl|
               ProperName 'и' ProperName Action_type Noun<gram='ins'>|
               Noun<gram='ins'> Action_type ProperName 'и' ProperName|
               Action_type Noun<gram='ins'> Scholar (Institution) 'и' Scholar (Institution)|
               Action_type Noun<gram='ins'> ProperName 'и' ProperName|
               Noun<gram='ins'> Action_type Scholar (Institution) 'и' Scholar (Institution)|
               Scholar (Institution) 'и' Scholar (Institution) Noun<gram='ins'> Action_type|
               //Abbreviated names
               (Adj<gnc-agr[1]>) Status<gram='pl', gnc-agr[1]> (Institution) AbrName 'и' AbrName|
               AbrName 'и' AbrName Action_type|
               Action_type AbrName 'и' AbrName|
               AbrName 'и' AbrName Action_type Noun<gram='ins'>|
               Noun<gram='ins'> Action_type AbrName 'и' AbrName ;

//Define actions going after the scholar's name
Action -> Verb<kwtype='scholar_action'> ;
Action_pres_sg -> Action<gram='praes,sg'> ;
Action_past_sg -> Action<gram='praet,sg'> ;
Action_pres_pl -> Action<gram='praes,pl'> ;
Action_past_pl -> Action<gram='praet,pl'> ;
Action_type -> Action_pres_sg | Action_past_sg |
               Action_pres_pl | Action_past_pl ;


//Define affiliation

Abbreviation -> Word<h-reg2>+; 
Location -> ProperName<gram='gen'> | 'в' ProperName<gram='abl'> ; 


Institution -> 'из' (Adj<gnc-agr[1]>+) Noun<kwtype='institution', gram='gen', rt, gnc-agr[1]> 
             (Location+)  | 
            (Adj<gnc-agr[1]>+) Noun<kwtype='institution', gram='gen', rt, gnc-agr[1]>
            (Location+)|
            Abbreviation;


//Define Possessive Pronouns
Pro -> Word<gram='APRO,abl'> ;

//Define Date
Year -> 'в' AnyWord<wff=/[1-2]?[0-9]{1,3}г?\.?/> ('год' <gram='sg,dat'>);

Century -> 'в' AnyWord<wff=/[1-2]?[0-9]{1,3}/> ('век' <gram='sg,abl'>)|
           'в' AnyWord<wff=/(XC|XL|X{0,3})(IX|IV|V?I{0,3})в?\.?/> ('век' <gram='sg,abl'>)|
           AnyWord<wff=/[1-2]?[0-9]{1,3}/> ('век' <gram='sg,gen'>)|
           AnyWord<wff=/(XC|XL|X{0,3})(IX|IV|V?I{0,3})в?\.?/> ('век' <gram='sg,gen'>) ;

Date -> Year | Century ; //Correct splitter for abbreviated dates 

//Citation
Citation -> 'по' Noun<kwtype='citation', gram='dat,pl'> ProperName<gram='gen, sg'> (Institution) |
            'в' Noun<kwtype='citation', gram='abl,pl'> ProperName<gram='gen, sg'> (Institution) |
            Noun<kwtype='citation', gram='nom,sg'> ProperName<gram='gen,sg'> (Institution)|
            'в' Noun<kwtype='citation', gram='abl,sg'>  ProperName<gram='gen,sg'> (Institution)|

            ProperName 'в'(Pro) Noun<kwtype='citation', gram='abl,sg'> |
            ProperName 'в' (Pro) Noun<kwtype='citation', gram='abl,pl'> ;

Citation_pl -> 'по' Noun<kwtype='citation', gram='dat,pl'> ProperName<gram='gen, sg'> (Institution) 
               'и' ProperName<gram='gen, sg'> (Institution) |
               'в' Noun<kwtype='citation', gram='abl,pl'> ProperName<gram='gen, sg'> (Institution) 'и'
               ProperName<gram='gen, sg'> (Institution)|
               Noun<kwtype='citation', gram='nom,sg'> ProperName<gram='gen,sg'> (Institution) 'и'
               ProperName<gram='gen, sg'> (Institution)|
               'в' Noun<kwtype='citation', gram='abl,sg'>  ProperName<gram='gen,sg'> (Institution) 'и'
               ProperName<gram='gen, sg'> (Institution)|
               
               ProperName 'и' ProperName 'в' (Pro) Noun<kwtype='citation', gram='abl,sg'> (Institution) |
               ProperName 'и' ProperName 'в' (Pro) Noun<kwtype='citation', gram='abl,pl'> (Institution);

//Define term introduction 
Term -> Noun<gram='nom'> ('впервые') (Verb<gram='praet'>) Word<gram='V,brev'> ProperName<gram='ins'> |
        Noun<gram='nom'> (Verb<gram='praet'>) Word<gram='V,brev'> ('впервые') ProperName<gram='ins'> |
        Noun<gram='nom'> (Verb<gram='praet'>) ('впервые') Word<gram='V,brev'> ProperName<gram='ins'> |
        ProperName<gram='ins'> (Verb<gram='praet'>) ('впервые') Word<gram='V,brev'>  Noun<gram='nom'>
        ;

TermIntroduction -> Term Date | Date Term ;

//Define greatest scientisits
GreatestSch -> ProperName (Verb<gram='praet'>) Word<gram='ANUM,ins'> 'из'
               Adj<gram='supr'> Status Date |
               Word<gram='ANUM,nom'> 'из' Adj<gram='supr'> Status Date ProperName |
               ProperName Word<gram='ANUM,nom'> 'из' Adj<gram='supr'> Status Date;

// Define prize context
Prize -> ProperName 'лауреат'<gnc-agr[1], rt> Adj<gnc-agr[1]> 'премия'<gram='gen,sg', gnc-agr[1]> |
        'лауреат'<gnc-agr[1], rt> Adj<gnc-agr[1]> 'премия'<gram='gen,sg', gnc-agr[1]> ProperName|
        Scholar (Institution) 'лауреат'<gnc-agr[1], rt> Adj<gnc-agr[1]> 'премия'<gram='gen,sg', gnc-agr[1]> |
        'лауреат'<gnc-agr[1], rt> Adj<gnc-agr[1]> 'премия'<gram='gen,sg', gnc-agr[1]> Scholar (Institution) |
        ProperName Action_type Adj<gnc-agr[1]> 'премия'<gram='acc,sg', gnc-agr[1]>|
        Scholar (Institution) Action_type Adj<gnc-agr[1]> 'премия'<gram='acc,sg', gnc-agr[1]>;


S -> Scholar (Institution) (Action_type) | Scholars_pl (Institution) (Action_type) |
    (Action_type) Scholars_pl (Institution) |
     Date Scholar (Institution) | Date Scholars_pl (Institution) | TermIntroduction | GreatestSch |
     Prize ;


//S -> Prize;


