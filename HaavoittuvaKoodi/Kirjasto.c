/*TEHTÄVÄ 1 - KIRJASTO
Etsi mahdolliset haavoittuvuudet ja pyri korjaamaan koodia.
Käytä esim. valgrind-ohjelmaa koodin analysointiin
*/
#include <stdio.h>
#define MAX_KIRJAN_NIMI 10
#define MAX_KIRJAILIJAN_NIMI 10
struct kirja {
       char nimi [MAX_KIRJAN_NIMI];
       char kirjailija [MAX_KIRJAILIJAN_NIMI];
       float hinta;
};
int main (void)
{
     struct kirja book;
     printf ("Anna kirjan nimi : ");
     gets(book.nimi);
     printf ("Anna kirjailijan nimi: ");
     gets (book.kirjailija);
     printf ("Anna kirjan hinta: ");
     scanf ("%f",&book.hinta);
     printf ("Annoit seuraavat tiedot: \n\n");
     /* Tulostukset 30 alkion levyisiin tulostuskenttiin */
     printf ("%-15s %-15s Hinta\n" ,"Kirjan nimi","Kirjoittaja");
     printf ("\n%-10s %-10s %6.2f\n",  book.nimi, book.kirjailija, book.hinta);
     return 0;
}