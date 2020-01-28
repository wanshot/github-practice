export default {
  beforeRouteLeave(to, from, _next) {
    const next = () => {
      this.unbind()
      _next()
    }
    if (this.isChanged) {
      this.confirmPageLeave(next)
      return
    }
    next()
  },
  data() {
    return {
    }
  },
  computed: {
    originalArticle() {
      const { relative } = this.$route.query
      return this.$store.getters['article/getArticleByRelative'](relative)
    },
    isChanged() {
      return !this.originalArticle.equals(this.edittingArticle)
    },
  },
  methods: {
    unbind() {
      window.removeEventListener('beforeunload', this.onBeforeUnload)
    },
    async update() {
      const loading = this.$loading.open()
      const { error, data } = await this.$store.dispatch('article/updateArticles', {
        article: this.edittingArticle
      })
      loading.close()
      if (error) {
        this.$dialog.alert({
          title: 'Error',
          message: error,
          type: 'is-danger',
        })
        return
      }
      this.$router.push('/admin/article/edit?relative=' + data.getRelative())
      await this.$nextTick()
      this.edittingArticle = this.originalArticle.copy()
      this.$toast.open({
        message: `Updated "${ this.edittingArticle.title }"`,
      })
    },
    async tryDelete() {
      this.$dialog.confirm({
        title: 'Confim delete',
        message: `OK to delete 「${ this.edittingArticle.slug }」`,
        cancelText: 'Cancel',
        confirmText: 'OK',
        type: 'is-danger',
        onConfirm: () => { this.delete() }
      })
    },
    async delete() {
      const loading = this.$loading.open()
      const { error } = await this.$store.dispatch('article/deleteArticles', {
        article: this.edittingArticle
      })
      loading.close()
      if (error) {
        this.$dialog.alert({
          title: 'Error',
          message: error,
          type: 'is-danger',
        })
        return
      }
      this.$router.push('/admin/article')
      await this.$store.dispatch('article/fetchArticles')
      this.$toast.open({
        message: `Deleted "${ this.edittingArticle.title }"`,
      })
    },
    confirmPageLeave(cb) {
      this.$dialog.confirm({
        message: this.changedAlertMessage,
        cancelText: 'Cancel',
        confirmText: 'OK',
        type: 'is-danger',
        onConfirm: () => cb()
      })
    },
  },
}
</script>
