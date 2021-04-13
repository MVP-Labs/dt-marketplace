import {
  Button,
  message,
  Modal,
  notification,
  Input,
  Dropdown,
  Menu,
  Icon,
} from "ant-design-vue";

export default (Vue) => {
  Vue.use(Button);
  Vue.use(Input);
  Vue.use(Dropdown);
  Vue.use(Menu);
  Vue.use(Icon);
  Vue.prototype.$confirm = Modal.confirm;
  Vue.prototype.$message = message;
  Vue.prototype.$modal = Modal;
  Vue.prototype.$notification = notification;
};
