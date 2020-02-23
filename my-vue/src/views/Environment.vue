<template>
  <div id="environment">
    <b-alert show variant="primary">
      <h2 class="subtitle">環境</h2>
    </b-alert>
    <div clss="environment_menu">
      <nav id="navbar-example2" class="navbar navbar-light bg-light">
        <ul class="nav nav-pills">
          <li class="nav-item">
          <a class="nav-link" href="#box-aws">AWS</a>
          </li>
          <li class="nav-item">
          <a class="nav-link" href="#box-django">Django</a>
          </li>
          <li class="nav-item">
          <a class="nav-link" href="#box-gunicorn">Gunicorn</a>
          </li>
          <li class="nav-item">
          <a class="nav-link" href="#box-nginx">Nginx</a>
          </li>
          <li class="nav-item">
          <a class="nav-link" href="#box-vuejs">Vue.js</a>
          </li>
          <li class="nav-item">
          <a class="nav-link" href="#box-boostrap">Bootstrap</a>
          </li>
          </ul>
        </nav>
        </div>
        <div data-spy="scroll" data-target="#navbar-example2" data-ofset="0">
          <h3 id="box-environment">当サイトの環境</h3>
          <h4 id="box-aws">AWS</h4>
          <p class="subtext">全てAWSで構築しています。Nginxでvue.jsを動かしているWebサーバーがあるPublicサブネット、MariaDBサーバーのあるPrivateサブネット、Gunicornでdjangoを動かしているAPIサーバーのあるPrivateサブネット、計3つのサブネットがVPC内にあります。</p><br><br>
          <h4 id="box-django">Django</h4>
          <p class="subtext">APIサーバーを書きました。REST APIでフロントからのリクエストを処理します。</p><br><br>
          <h4 id="box-gunicorn">Gunicorn</h4>
          <p class="subtext">djangoを動かしてます。APIサーバー。nginxとMariaDBとの中間。MariaDBからデータを取りに/書き込みにいきます。</p><br><br>
          <h4 id="box-nginx">Nginx</h4>
          <p class="subtext">フロントのサーバーです。vue.jsで作ったjsをメインに主にクライアントとやり取りしています。ページ内にDBのデータが必要/DBに書き込む時はクライアントJSの要求を受けてプロキシサーバーとしてAPIに接続しデータを引っ張ってきます。</p><br><br>
          <h4 id="box-vuejs">Vue.js</h4>
          <p class="subtext">jsはこれで書いてます。vue-routerを使ってSPAにしました。axiosでNginxのリバースプロキシ越しに入力/投稿一覧フォームのデータを取ります。</p><br><br>
          <h4 id="box-bootstrap">Bootstrap Bootstrap-vue</h4>
          <p class="subtext">ここに書くものでは無いかもしれませんが、デザインで多用したので入れておきました。</p><br><br>
    </div>
    <b-img src="@/assets/aws.png" fluid alt="Responsive image"></b-img>
  </div>
</template>

<script>
export default {
}
</script>

<style scoped>
#body-scroll {
}
</style>