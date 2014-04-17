VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "chef/ubuntu-13.10"
  #config.vm.network :forwarded_port, guest: 80, host: 8888
  config.vm.network :private_network, ip: "10.42.42.100"
  config.vm.synced_folder ".", "/projects/openstates/src/site"
  config.vm.synced_folder "../billy", "/projects/openstates/src/billy"

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.name = "openstates.org"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/site.yml"
    ansible.inventory_path = "ansible/hosts.vagrant"
    ansible.limit = "all"
    ansible.extra_vars = { vagrant: true }
  end
end
