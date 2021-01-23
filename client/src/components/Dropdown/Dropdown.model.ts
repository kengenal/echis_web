export interface DropdownList {
  header: {
    label?: string;
    icon?: string;
    image?: string;
  };
  items: {
    label: string;
    link: string;
    icon: string;
  }[];
}
