#encoding "utf-8" 
#GRAMMAR_ROOT S 

 
//Define Names  
//ProperName ->  Word<h-reg1>+ |  Word<h-reg1, gram='f'>+ ; 
Name -> Word<wfm=/[А-Я][а-я-]+/> ;
ProperName -> Name+ ;
Person -> ProperName<~fw> interp (Person.Name::not_norm) ;



//Define names with initials (abbreviated name)
Initial -> AnyWord<wff=/[А-ЯЁ]\./> ;
Initials -> Initial+ ;
AbrName ->  Word<h-reg1> Initials | Word<h-reg1, gram='f'> Initials |
            Initials  Word<h-reg1> | Initials Word<h-reg1, gram='f'> ;
AbbreviatedName -> AbrName interp (Person.Name) ;

//Define scholar status
Status -> Noun<kwtype='scholar_status'> interp (Person.Status);

//Define Scholar non-terminal

Scholar ->  (Adj<gnc-agr[1]>) Status<gnc-agr[1], gram='sg'> Person<gnc-agr[1], rt> |
            (Adj<gnc-agr[1]>) Person<gnc-agr[1], rt> Status<gnc-agr[1], gram='sg'> |           
            Citation |
            Person Action_type |
            //feminitive agreement with ProperName
             (Adj<fem-c-agr[1]>) Status<fem-c-agr[1], gram='sg'> Person<fem-c-agr[1], rt>| 
             (Adj<fem-c-agr[1]>) Person<fem-c-agr[1], rt> Status<fem-c-agr[1], gram='sg'>|
             //Abbreviated names 
            (Adj<gnc-agr[1]>) Status<gnc-agr[1], gram='sg'> AbbreviatedName<gnc-agr[1], rt> |
            (Adj<gnc-agr[1]>) AbbreviatedName<gnc-agr[1], rt> Status<gnc-agr[1], gram='sg'> |
            //Abbreviated fem names
            (Adj<fem-c-agr[1]>) Status<fem-c-agr[1], gram='sg'> AbbreviatedName<fem-c-agr[1], rt>| 
            (Adj<fem-c-agr[1]>) AbbreviatedName<fem-c-agr[1], rt> Status<fem-c-agr[1], gram='sg'>
            ; 

//Define scholars plural contexts
Scholars_pl -> Scholar (Institution) 'и' Scholar (Institution) |
               (Adj<gnc-agr[1]>) Status<gram='pl', gnc-agr[1], rt> (Institution) Person 'и' Person|
               Person 'и' Person Action_type<gram='pl'>|
               Action_type<gram='pl'> Person 'и' Person|
               Citation_pl|
               Person 'и' Person Action_type Noun<gram='ins'>|
               Noun<gram='ins'> Action_type Person 'и' Person|
               Action_type Noun<gram='ins'> Scholar (Institution) 'и' Scholar (Institution)|
               Action_type Noun<gram='ins'> Person 'и' Person|
               Noun<gram='ins'> Action_type Scholar (Institution) 'и' Scholar (Institution)|
               Scholar (Institution) 'и' Scholar (Institution) Noun<gram='ins'> Action_type|
               //Abbreviated names
               (Adj<gnc-agr[1]>) Status<gram='pl', gnc-agr[1], rt> (Institution) AbbreviatedName 'и' AbbreviatedName|
               AbbreviatedName 'и' AbbreviatedName Action_type|
               Action_type AbbreviatedName 'и' AbbreviatedName|
               AbbreviatedName 'и' AbbreviatedName Action_type Noun<gram='ins'>|
               Noun<gram='ins'> Action_type AbbreviatedName 'и' AbbreviatedName ;

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
Location -> ProperName<gram='gen'> | 'в' ProperName<gram='abl'> | Abbreviation ; 


Institution -> 'из' (Adj<gnc-agr[1]>+) Noun<kwtype='institution', gram='gen', rt, gnc-agr[1]> 
             (Location+)  | 
            (Adj<gnc-agr[1]>+) Noun<kwtype='institution', gram='gen', rt, gnc-agr[1]>
            (Location+);


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
Citation -> 'по' Noun<kwtype='citation', gram='dat,pl'> Person<gram='gen, sg'> (Institution) |
            'в' Noun<kwtype='citation', gram='abl,pl'> Person<gram='gen, sg'> (Institution) |
            Noun<kwtype='citation', gram='nom,sg'> Person<gram='gen,sg'> (Institution)|
            'в' Noun<kwtype='citation', gram='abl,sg'>  Person<gram='gen,sg'> (Institution)|

            Person 'в'(Pro) Noun<kwtype='citation', gram='abl,sg'> |
            Person 'в' (Pro) Noun<kwtype='citation', gram='abl,pl'> ;

Citation_pl -> 'по' Noun<kwtype='citation', gram='dat,pl'> Person<gram='gen, sg'> (Institution) 
               'и' Person<gram='gen, sg'> (Institution) |
               'в' Noun<kwtype='citation', gram='abl,pl'> Person<gram='gen, sg'> (Institution) 'и'
               Person<gram='gen, sg'> (Institution)|
               Noun<kwtype='citation', gram='nom,sg'> Person<gram='gen,sg'> (Institution) 'и'
               Person<gram='gen, sg'> (Institution)|
               'в' Noun<kwtype='citation', gram='abl,sg'>  Person<gram='gen,sg'> (Institution) 'и'
               Person<gram='gen, sg'> (Institution)|
               
               Person 'и' Person 'в' (Pro) Noun<kwtype='citation', gram='abl,sg'> (Institution) |
               Person 'и' Person 'в' (Pro) Noun<kwtype='citation', gram='abl,pl'> (Institution);

//Define term introduction 
Term -> Noun<gram='nom'> ('впервые') (Verb<gram='praet'>) Word<gram='V,brev'> Person<gram='ins'> |
        Noun<gram='nom'> (Verb<gram='praet'>) Word<gram='V,brev'> ('впервые') Person<gram='ins'> |
        Noun<gram='nom'> (Verb<gram='praet'>) ('впервые') Word<gram='V,brev'> Person<gram='ins'> |
        Person<gram='ins'> (Verb<gram='praet'>) ('впервые') Word<gram='V,brev'>  Noun<gram='nom'>
        ;

TermIntroduction -> Term Date | Date Term ;

//Define greatest scientisits
GreatestSch -> Person (Verb<gram='praet'>) Word<gram='ANUM,ins'> 'из'
               Adj<gram='supr'> Status Date |
               Word<gram='ANUM,nom'> 'из' Adj<gram='supr'> Status Date Person |
               Person Word<gram='ANUM,nom'> 'из' Adj<gram='supr'> Status Date;

// Define prize context
Prize -> Person 'лауреат'<gnc-agr[1], rt> Adj<gnc-agr[1]> 'премия'<gram='gen,sg', gnc-agr[1]> |
        'лауреат'<gnc-agr[1], rt> Adj<gnc-agr[1]> 'премия'<gram='gen,sg', gnc-agr[1]> Person|
        Scholar (Institution) 'лауреат'<gnc-agr[1], rt> Adj<gnc-agr[1]> 'премия'<gram='gen,sg', gnc-agr[1]> |
        'лауреат'<gnc-agr[1], rt> Adj<gnc-agr[1]> 'премия'<gram='gen,sg', gnc-agr[1]> Scholar (Institution) |
        Person Action_type Adj<gnc-agr[1]> 'премия'<gram='acc,sg', gnc-agr[1]>|
        Scholar (Institution) Action_type Adj<gnc-agr[1]> 'премия'<gram='acc,sg', gnc-agr[1]>;


S -> Scholar (Institution) (Action_type) | Scholars_pl (Institution) (Action_type) |
    (Action_type) Scholars_pl (Institution) |
     Date Scholar (Institution) | Date Scholars_pl (Institution) | TermIntroduction | GreatestSch |
     Prize ;


//S -> Prize ;


