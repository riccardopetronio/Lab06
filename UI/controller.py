import copy

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.retailer = None

    def fill_dd_anno(self):
        anni = self._model.get_anni()
        for i in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option( i ))
        self._view.update_page()


    def fill_dd_brand(self):
        brand = self._model.get_brand()
        for i in brand:
            self._view.dd_brand.options.append(ft.dropdown.Option( i ))
        self._view.update_page()

    def fill_dd_retailer(self):
        retailer = self._model.get_retailer()
        for r in retailer:
            self._view.dd_retailer.options.append(ft.dropdown.Option(
            key= r.Retailer_code,
            data=r,
            text= r.Retailer_name,
            on_click=self.seleziona_retailer
            ))
        self._view.update_page()

    def seleziona_retailer(self, event):
        self.retailer = event.control.data

    def top_vendite(self, event):
        self._view.txt_result.controls.clear()
        self._view.update_page()

        anno_selezionato = self._view.dd_anno.value
        brand_selezionato = self._view.dd_brand.value

        if anno_selezionato is None or brand_selezionato is None:
            self._view.create_alert("devi riempire tutti i campi")
            return

        tutte_le_vendite = self._model.get_top_vendite()

        if self._view.dd_anno.value != "Nessun Filtro":
            lista_filtrata = [v for v in tutte_le_vendite if v.data.startswith(anno_selezionato)]
        else:
            lista_filtrata = copy.deepcopy(tutte_le_vendite)

        if self._view.dd_brand.value != "Nessun Filtro":
            codici_prodotto = self._model.get_codici_prodotto_brand(self._view.dd_brand.value)
            lista_filtrata2 = [v for v in lista_filtrata if v.product_number in codici_prodotto]
        else:
            lista_filtrata2 = copy.deepcopy(lista_filtrata)

        if self._view.dd_retailer.value != "Nessun Filtro":
            lista_filtrata3 = [v for v in lista_filtrata2 if v.retailer_code == self.retailer.Retailer_code]
        else:
            lista_filtrata3 = copy.deepcopy(lista_filtrata2)

        lunghezza_risultato = lista_filtrata3.__len__()
        if lunghezza_risultato <= 5:
            self._view.txt_result.controls.append(ft.Text( f"solo {lunghezza_risultato} elementi" ))
        else:
            lunghezza_risultato = 5

        for v in range(0, lunghezza_risultato):
            self._view.txt_result.controls.append(ft.Text( lista_filtrata3[v] ))
        self._view.update_page()

    def analizza_vendite(self, event):
        self._view.txt_result.controls.clear()
        self._view.update_page()

        anno_selezionato = self._view.dd_anno.value
        brand_selezionato = self._view.dd_brand.value

        if anno_selezionato is None or brand_selezionato is None:
            self._view.create_alert("devi riempire tutti i campi")
            return

        tutte_le_vendite = self._model.get_top_vendite()

        if self._view.dd_anno.value != "Nessun Filtro":
            lista_filtrata = [v for v in tutte_le_vendite if v.data.startswith(anno_selezionato)]
        else:
            lista_filtrata = copy.deepcopy(tutte_le_vendite)

        if self._view.dd_brand.value != "Nessun Filtro":
            codici_prodotto = self._model.get_codici_prodotto_brand(self._view.dd_brand.value)
            lista_filtrata2 = [v for v in lista_filtrata if v.product_number in codici_prodotto]
        else:
            lista_filtrata2 = copy.deepcopy(lista_filtrata)

        if self._view.dd_retailer.value != "Nessun Filtro":
            lista_filtrata3 = [v for v in lista_filtrata2 if v.retailer_code == self.retailer.Retailer_code]
        else:
            lista_filtrata3 = copy.deepcopy(lista_filtrata2)

        lunghezza_risultato = lista_filtrata3.__len__()
        if lunghezza_risultato <= 5:
            self._view.txt_result.controls.append(ft.Text(f"solo {lunghezza_risultato} elementi"))
        else:
            lunghezza_risultato = 5

        tot_ricavi = 0
        n_retailers = set()
        n_prodotti = set()
        for v in lista_filtrata3:
            tot_ricavi += v.ricavo
            n_retailers.add(v.retailer_code)
            n_prodotti.add(v.product_number)

        self._view.txt_result.controls.append(ft.Text("Statistiche vendite:"))
        self._view.txt_result.controls.append(ft.Text(f"Giro d'affari: {tot_ricavi}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero vendite: {lista_filtrata3.__len__()}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero retailers coinvolti {n_retailers.__len__()}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero prodotti coinvolti {n_prodotti.__len__()}"))

        self._view.update_page()
