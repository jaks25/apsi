<template>
    <div class="main-body">
        <!--Grey area section-->
        <section class="grey lighten-4 text-center width-100">
            <search-section />
            <categories-picker
                :categories=categories
                :onCategoryClick=loadAdsByCategory
            />
        </section>
        <section v-if="isSearched">
            <highlights-list
                title="Ogłoszenia promowane"
                column="true"
                :items=searchedAds
            />
        </section>
        <section v-else>
            <!--White area section-->
            <highlights-list
                title="Ogłoszenia promowane"
                :items=promotedItems
            />
            <highlights-list
                title="Ostatnio dodane"
                :items=lastAdded
            />
        </section>
    </div>
</template>

<script>
    import CategoriesPicker from "@/components/CategoriesPicker";
    import HighlightsList from "@/components/HighlightsList";
    import SearchSection from "@/components/SearchSection";
    export default {
        name: 'Home',
        components: { HighlightsList, CategoriesPicker, SearchSection},
        data: () => {
            return {
                    promotedItems: [
                        { title: 'Promowany 1', price: "3", id: '0'}, 
                        { title: 'Promowany 2', price: "300", id: '0'}, 
                        { title: 'Promowany 3', price: "123", id: '0'}
                    ],
                    lastAdded: [
                        { title: 'Ostatnio dodany 1', price: "54", id: '0'}, 
                        { title: 'Ostatnio dodany 2', price: "124", id: '0'}, 
                        { title: 'Ostatnio dodany 3', price: "500", id: '0'}
                    ],
                    categories: [
                        { icon: 'mdi-car', name: 'Motoryzacja' },
                        { icon: 'mdi-home', name: 'Nieruchomości' },
                        { icon: 'mdi-worker', name: 'Praca' },
                        { icon: 'mdi-sofa', name: 'Dom i ogród' },
                        { icon: 'mdi-laptop', name: 'Elektronika' },
                        { icon: 'mdi-tshirt-crew', name: 'Moda' },
                        { icon: 'mdi-dog-side', name: 'Zwierzęta' },
                        { icon: 'mdi-human-child', name: 'Dla dzieci' },
                        { icon: 'mdi-basketball', name: 'Sport' },
                        { icon: 'mdi-book-open', name: 'Edukacja' },
                        { icon: 'mdi-guitar-acoustic', name: 'Muzyka' },
                        { icon: 'mdi-postage-stamp', name: 'Hobby' }
                    ],
                    isSearched: false,
                    searchedAds: []
                }
        },
        methods: {
            loadAdsByCategory: async function(categoryName) {
                    try {
                        const resp = await this.$http.get(`/api/adverts/`, { params: { advert_category: categoryName } });
                        this.searchedAds = resp.data;
                        this.isSearched = true
                    } catch {
                       console.log("kek") 
                    }
                }
            }
    }
</script>

<style scoped>
    .main-body {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding-bottom: 10rem;
    }

    .width-100 {
        width: 100%;
    }
</style>
