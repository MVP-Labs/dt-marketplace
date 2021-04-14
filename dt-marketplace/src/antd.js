import {
  Button,
  message,
  Modal,
  notification,
  Input,
  Dropdown,
  Menu,
  Icon,
  Card,
  Spin,
  Table,
} from "ant-design-vue";

export default (Vue) => {
  Vue.use(Button);
  Vue.use(Input);
  Vue.use(Dropdown);
  Vue.use(Menu);
  Vue.use(Icon);
  Vue.use(Card);
  Vue.use(Spin);
  Vue.use(Table);
  Vue.use(Modal);
  Vue.prototype.$confirm = Modal.confirm;
  Vue.prototype.$message = message;
  Vue.prototype.$modal = Modal;
  Vue.prototype.$notification = notification;
};
